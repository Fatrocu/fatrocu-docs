param(
    [Parameter(Mandatory=$true)]
    [ValidatePattern('^[0-9a-fA-F]{40}$')]
    [string]$ExpectedMainCommit,
    [switch]$Refresh,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
$repositoryUrl = 'https://github.com/Fatrocu/fatrocu-docs'
$repository = Invoke-RestMethod -Uri 'https://api.github.com/repos/Fatrocu/fatrocu-docs'
if ($repository.private -or $repository.default_branch -ne 'main') {
    throw 'OpenWiki requires the reviewed public documentation repository on main'
}
$revision = Invoke-RestMethod -Uri 'https://api.github.com/repos/Fatrocu/fatrocu-docs/commits/main'
if ($revision.sha -ne $ExpectedMainCommit) {
    throw 'Main does not match the reviewed documentation revision. No wiki request was sent.'
}
$intent = [ordered]@{
    repository = $repositoryUrl
    source_commit = $revision.sha
    wiki_url = 'https://openwiki.sh/Fatrocu/fatrocu-docs'
    force = [bool]$Refresh
}
if ($DryRun) {
    $intent | ConvertTo-Json
    exit 0
}
$body = @{ repoUrl=$repositoryUrl; force=[bool]$Refresh } | ConvertTo-Json
$result = Invoke-RestMethod -Method Post -Uri 'https://openwiki.sh/api/repositories' -ContentType 'application/json' -Body $body
[ordered]@{
    submission=$intent
    job=$result.job
    repository=$result.repository
    publication='Verify indexing and citations before claiming publication complete'
} | ConvertTo-Json -Depth 8
