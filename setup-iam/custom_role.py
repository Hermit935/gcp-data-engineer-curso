import argparse
import os

from google.api_core import exceptions as google_exceptions


def create_custom_role(project_id, role_id, title="VM Starter Stopper", permissions=None):
    """
    Create a custom IAM role in the specified project.

    Args:
        project_id (str): The ID of the Google Cloud project.
        role_id (str): The ID of the custom role to create.
        title (str): The friendly title for the role.
        permissions (list[str] | None): Permissions to include in the role.

    Returns:
        The created custom role object.
    """
    try:
        from google.cloud import iam_admin_v1
    except ImportError as exc:
        raise SystemExit(
            "Falta la dependencia de Google Cloud. Instálala con: pip install google-cloud-iam"
        ) from exc

    if permissions is None:
        permissions = ["compute.instances.start", "compute.instances.stop"]

    client = iam_admin_v1.IAMClient()
    parent = f"projects/{project_id}"

    role_kwargs = {
        "title": title,
        "included_permissions": permissions,
    }

    if hasattr(iam_admin_v1.Role, "Stage"):
        role_kwargs["stage"] = iam_admin_v1.Role.Stage.GA

    role = iam_admin_v1.Role(**role_kwargs)

    request = iam_admin_v1.CreateRoleRequest(
        parent=parent,
        role_id=role_id,
        role=role,
    )

    try:
        response = client.create_role(request=request)
    except google_exceptions.PermissionDenied as exc:
        raise SystemExit(
            "No tienes permiso para crear roles IAM en este proyecto. "
            "Autentica con un usuario que tenga el rol roles/iam.organizationRoleAdmin o roles/iam.roleAdmin "
            "y verifica el proyecto con 'gcloud config set project <PROJECT_ID>'."
        ) from exc
    except Exception as exc:
        raise SystemExit(f"No se pudo crear el rol IAM: {exc}") from exc

    print(f"Rol Creado: {response.name}")
    return response


def parse_args():
    parser = argparse.ArgumentParser(description="Crear un rol IAM personalizado en GCP")
    parser.add_argument("project_id", nargs="?", default=None, help="ID del proyecto de Google Cloud")
    parser.add_argument("role_id", nargs="?", default=None, help="ID del rol personalizado")
    parser.add_argument("--project-id", dest="project_id_opt", default=None, help="ID del proyecto de Google Cloud")
    parser.add_argument("--role-id", dest="role_id_opt", default=None, help="ID del rol personalizado")
    parser.add_argument("--title", default="VM Starter Stopper", help="Título amigable del rol")
    parser.add_argument(
        "--permissions",
        nargs="*",
        default=["compute.instances.start", "compute.instances.stop"],
        help="Permisos a incluir en el rol",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    project_id = args.project_id_opt or args.project_id or os.getenv("GCP_PROJECT_ID")
    role_id = args.role_id_opt or args.role_id or os.getenv("GCP_ROLE_ID", "vmStarterStopper")

    if not project_id:
        raise SystemExit(
            "Debes proporcionar el proyecto con un argumento posicional, --project-id o la variable GCP_PROJECT_ID"
        )

    create_custom_role(project_id, role_id, title=args.title, permissions=args.permissions)


if __name__ == "__main__":
    main()