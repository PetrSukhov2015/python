from jira import JIRA

# Параметры подключения
jira_options = {'server': 'https://jira.hi-tech.org/'}
jira = JIRA(options=jira_options, basic_auth=('petr.sukhov','PASSWord'))

# JQL-запрос
jql_query = 'project = VCSWEB and fixVersion = 25.0'
issues = jira.search_issues(jql_query)
#print(issues)
# Вывод результатов
for issue in issues:
    print(f"Задача: {issue.key} {issue.fields.summary}")