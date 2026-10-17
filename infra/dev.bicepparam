using './main.bicep'
param env = 'dev'
param appName = 'func-cmsdev-pawan-dev'
param greeting = 'Hello from DEV'
param appVersion = readEnvironmentVariable('APP_VERSION', 'manual')
