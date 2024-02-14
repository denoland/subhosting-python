# Shared Types

```python
from subhosting.types import Analytics, Deployment, Domain, KvDatabase, Project
```

# Organizations

Types:

```python
from subhosting.types import Organization
```

Methods:

- <code title="get /organizations/{organizationId}">client.organizations.<a href="./src/subhosting/resources/organizations/organizations.py">get</a>(organization_id) -> <a href="./src/subhosting/types/organization.py">Organization</a></code>

## Analytics

Methods:

- <code title="get /organizations/{organizationId}/analytics">client.organizations.analytics.<a href="./src/subhosting/resources/organizations/analytics.py">get</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/analytics_get_params.py">params</a>) -> <a href="./src/subhosting/types/shared/analytics.py">Analytics</a></code>

## Projects

Types:

```python
from subhosting.types.organizations import ProjectListResponse
```

Methods:

- <code title="post /organizations/{organizationId}/projects">client.organizations.projects.<a href="./src/subhosting/resources/organizations/projects.py">create</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/project_create_params.py">params</a>) -> <a href="./src/subhosting/types/shared/project.py">Project</a></code>
- <code title="get /organizations/{organizationId}/projects">client.organizations.projects.<a href="./src/subhosting/resources/organizations/projects.py">list</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/project_list_params.py">params</a>) -> <a href="./src/subhosting/types/organizations/project_list_response.py">ProjectListResponse</a></code>

## Databases

Types:

```python
from subhosting.types.organizations import DatabaseListResponse
```

Methods:

- <code title="post /organizations/{organizationId}/databases">client.organizations.databases.<a href="./src/subhosting/resources/organizations/databases.py">create</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/database_create_params.py">params</a>) -> <a href="./src/subhosting/types/shared/kv_database.py">KvDatabase</a></code>
- <code title="get /organizations/{organizationId}/databases">client.organizations.databases.<a href="./src/subhosting/resources/organizations/databases.py">list</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/database_list_params.py">params</a>) -> <a href="./src/subhosting/types/organizations/database_list_response.py">DatabaseListResponse</a></code>

## Domains

Types:

```python
from subhosting.types.organizations import DomainListResponse
```

Methods:

- <code title="post /organizations/{organizationId}/domains">client.organizations.domains.<a href="./src/subhosting/resources/organizations/domains.py">create</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/domain_create_params.py">params</a>) -> <a href="./src/subhosting/types/shared/domain.py">Domain</a></code>
- <code title="get /organizations/{organizationId}/domains">client.organizations.domains.<a href="./src/subhosting/resources/organizations/domains.py">list</a>(organization_id, \*\*<a href="src/subhosting/types/organizations/domain_list_params.py">params</a>) -> <a href="./src/subhosting/types/organizations/domain_list_response.py">DomainListResponse</a></code>

# Databases

Methods:

- <code title="patch /databases/{databaseId}">client.databases.<a href="./src/subhosting/resources/databases.py">update</a>(database_id, \*\*<a href="src/subhosting/types/database_update_params.py">params</a>) -> <a href="./src/subhosting/types/shared/kv_database.py">KvDatabase</a></code>

# Projects

Methods:

- <code title="patch /projects/{projectId}">client.projects.<a href="./src/subhosting/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/subhosting/types/project_update_params.py">params</a>) -> <a href="./src/subhosting/types/shared/project.py">Project</a></code>
- <code title="delete /projects/{projectId}">client.projects.<a href="./src/subhosting/resources/projects/projects.py">delete</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}">client.projects.<a href="./src/subhosting/resources/projects/projects.py">get</a>(project_id) -> <a href="./src/subhosting/types/shared/project.py">Project</a></code>

## Analytics

Methods:

- <code title="get /projects/{projectId}/analytics">client.projects.analytics.<a href="./src/subhosting/resources/projects/analytics.py">get</a>(project_id, \*\*<a href="src/subhosting/types/projects/analytics_get_params.py">params</a>) -> <a href="./src/subhosting/types/shared/analytics.py">Analytics</a></code>

## Deployments

Types:

```python
from subhosting.types.projects import DeploymentListResponse
```

Methods:

- <code title="post /projects/{projectId}/deployments">client.projects.deployments.<a href="./src/subhosting/resources/projects/deployments.py">create</a>(project_id, \*\*<a href="src/subhosting/types/projects/deployment_create_params.py">params</a>) -> <a href="./src/subhosting/types/shared/deployment.py">Deployment</a></code>
- <code title="get /projects/{projectId}/deployments">client.projects.deployments.<a href="./src/subhosting/resources/projects/deployments.py">list</a>(project_id, \*\*<a href="src/subhosting/types/projects/deployment_list_params.py">params</a>) -> <a href="./src/subhosting/types/projects/deployment_list_response.py">DeploymentListResponse</a></code>

# Deployments

Methods:

- <code title="delete /deployments/{deploymentId}">client.deployments.<a href="./src/subhosting/resources/deployments/deployments.py">delete</a>(deployment_id) -> None</code>
- <code title="get /deployments/{deploymentId}">client.deployments.<a href="./src/subhosting/resources/deployments/deployments.py">get</a>(deployment_id) -> <a href="./src/subhosting/types/shared/deployment.py">Deployment</a></code>
- <code title="post /deployments/{deploymentId}/redeploy">client.deployments.<a href="./src/subhosting/resources/deployments/deployments.py">redeploy</a>(deployment_id, \*\*<a href="src/subhosting/types/deployment_redeploy_params.py">params</a>) -> <a href="./src/subhosting/types/shared/deployment.py">Deployment</a></code>

## BuildLogs

Types:

```python
from subhosting.types.deployments import BuildLogGetResponse
```

Methods:

- <code title="get /deployments/{deploymentId}/build_logs">client.deployments.build_logs.<a href="./src/subhosting/resources/deployments/build_logs.py">get</a>(deployment_id) -> <a href="./src/subhosting/types/deployments/build_log_get_response.py">BuildLogGetResponse</a></code>

## AppLogs

Types:

```python
from subhosting.types.deployments import AppLogGetResponse
```

Methods:

- <code title="get /deployments/{deploymentId}/app_logs">client.deployments.app_logs.<a href="./src/subhosting/resources/deployments/app_logs.py">get</a>(deployment_id, \*\*<a href="src/subhosting/types/deployments/app_log_get_params.py">params</a>) -> <a href="./src/subhosting/types/deployments/app_log_get_response.py">AppLogGetResponse</a></code>

# Domains

Methods:

- <code title="patch /domains/{domainId}">client.domains.<a href="./src/subhosting/resources/domains/domains.py">update</a>(domain_id, \*\*<a href="src/subhosting/types/domain_update_params.py">params</a>) -> None</code>
- <code title="delete /domains/{domainId}">client.domains.<a href="./src/subhosting/resources/domains/domains.py">delete</a>(domain_id) -> None</code>
- <code title="get /domains/{domainId}">client.domains.<a href="./src/subhosting/resources/domains/domains.py">get</a>(domain_id) -> <a href="./src/subhosting/types/shared/domain.py">Domain</a></code>
- <code title="post /domains/{domainId}/verify">client.domains.<a href="./src/subhosting/resources/domains/domains.py">verify</a>(domain_id) -> None</code>

## Certificates

Methods:

- <code title="post /domains/{domainId}/certificates">client.domains.certificates.<a href="./src/subhosting/resources/domains/certificates.py">create</a>(domain_id, \*\*<a href="src/subhosting/types/domains/certificate_create_params.py">params</a>) -> None</code>
- <code title="post /domains/{domainId}/certificates/provision">client.domains.certificates.<a href="./src/subhosting/resources/domains/certificates.py">provision</a>(domain_id) -> None</code>
