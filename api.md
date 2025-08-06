# AccountInfo

## V3

Types:

```python
from hbs.types.account_info import V3GetAccountDetailsResponse
```

Methods:

- <code title="get /account-info/v3/details">client.account_info.v3.<a href="./src/hbs/resources/account_info/v3/v3.py">get_account_details</a>() -> <a href="./src/hbs/types/account_info/v3_get_account_details_response.py">V3GetAccountDetailsResponse</a></code>

### Activity

Types:

```python
from hbs.types.account_info.v3 import (
    ForwardPaging,
    ActivityGetAuditLogsResponse,
    ActivityGetLoginActivityResponse,
    ActivityGetSecurityActivityResponse,
)
```

Methods:

- <code title="get /account-info/v3/activity/audit-logs">client.account_info.v3.activity.<a href="./src/hbs/resources/account_info/v3/activity.py">get_audit_logs</a>(\*\*<a href="src/hbs/types/account_info/v3/activity_get_audit_logs_params.py">params</a>) -> <a href="./src/hbs/types/account_info/v3/activity_get_audit_logs_response.py">ActivityGetAuditLogsResponse</a></code>
- <code title="get /account-info/v3/activity/login">client.account_info.v3.activity.<a href="./src/hbs/resources/account_info/v3/activity.py">get_login_activity</a>(\*\*<a href="src/hbs/types/account_info/v3/activity_get_login_activity_params.py">params</a>) -> <a href="./src/hbs/types/account_info/v3/activity_get_login_activity_response.py">ActivityGetLoginActivityResponse</a></code>
- <code title="get /account-info/v3/activity/security">client.account_info.v3.activity.<a href="./src/hbs/resources/account_info/v3/activity.py">get_security_activity</a>(\*\*<a href="src/hbs/types/account_info/v3/activity_get_security_activity_params.py">params</a>) -> <a href="./src/hbs/types/account_info/v3/activity_get_security_activity_response.py">ActivityGetSecurityActivityResponse</a></code>

### APIUsage

Types:

```python
from hbs.types.account_info.v3 import APIUsageGetDailyUsageResponse
```

Methods:

- <code title="get /account-info/v3/api-usage/daily">client.account_info.v3.api_usage.<a href="./src/hbs/resources/account_info/v3/api_usage.py">get_daily_usage</a>() -> <a href="./src/hbs/types/account_info/v3/api_usage_get_daily_usage_response.py">APIUsageGetDailyUsageResponse</a></code>
