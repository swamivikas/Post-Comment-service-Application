# technologies used
  1. Django
  2. sqlite database
  3. python
  4. beautifulsoup
  5. pillow
  6. html
  7. css, bootstrap
  




   preview of the project


   

https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/c1403d9b-36b2-408e-b41f-2823bbd26462


i cant upload more than 10 mb file so this is a short prview of  to do a comment 



# how to run locally 

   1. first of all create a virtual environment (make sure python is installed in your computer and path is added in environmental variables )
           create a virtual environment like this
           command -> python -m venv (name of your virtual environment) , sample is shown below
           <img width="697" alt="image" src="https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/43321f8a-ad2a-4ce8-a695-7010a0df065e">
   2. now activate your virtual environment
         1.command -> (your virtual environment name)\Scripts\Activate.bat   (for windows)
         2.command ->  source (your virtual environment name)/bin/activate    (for mac)  , sample is shown below for windows
         <img width="692" alt="image" src="https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/297db68c-98c9-4803-9635-2ba627229557">
   3. now install all dependencies :

      
         ![image](https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/d8b0146e-160c-44c0-be69-c3d2637cbb33)

  5. now apply migration to the database
       command ->  python manage.py migrate  , sample is shown below
       <img width="692" alt="image" src="https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/9a3e34b3-5223-4937-928b-8f5dea47cadf">

  6. now run the  server using following command
      command -> python manage.py runserver  , sample is shown below
      ![image](https://github.com/swamivikas/cloudsek-backend-intern-assignment-Post-Comment-service-Application/assets/108607735/2d7f62d0-a593-47a3-aaf1-9fbc8ffd6c3f)
    
   7. now your application will run on this server -> http://127.0.0.1:8000/     



# why i choose Django over other 
  Django has built-in features that make it safer to use the user-submitted data on the application
  and django is having inbuilt sqlite database however we cannot use its inbuilt database for large projects 

  and django also provides us these features 
   1. Battries included
   2. flexible and scalable
   4. easy to use
   5. active community (it addapts python community )


# lets see in action of this project 

  1. this is our home page 
    

![Screenshot 2024-05-12 181405](https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/60731d7c-0098-4371-81bb-2a0a70fb0b36)
    2. this is our sign up page (however we can use bootstrap on it and can make it more beautiful )
    
![Screenshot 2024-05-12 181415](https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/ff8249e3-b20e-4003-9007-cad287e10220)
    3. this our post create tab in this we can create post this post-create tab contains two arguments image and text (image you can select from flickr link is given just above from add url section )
    
 <img width="527" alt="cloudsek img" src="https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/56504ed5-d550-40d9-933f-c7af1c2fbdaf">
 
 4. comment section  - in this multiple users can comment on one post and those users username will show on their comment 
    

![Screenshot 2024-05-12 181456](https://github.com/swamivikas/CloudSek-Backend-Intern-Post-Comment-Assignment/assets/108607735/194dad12-41df-464d-9673-9e90d5377840)





























# Chainsaw Parallel Testing Guide

## Overview
This document explains how to effectively use Chainsaw for parallel test execution, particularly for running multiple policy validation tests concurrently in a Kubernetes environment.

## Table of Contents
1. [Parallel Test Execution](#parallel-test-execution)
2. [Concurrency Management](#concurrency-management)
3. [Namespace Isolation](#namespace-isolation)
4. [Test Structure](#test-structure)
5. [Go Integration](#go-integration)
6. [Best Practices](#best-practices)

## Parallel Test Execution

### Basic Usage
To run tests in parallel, use the `--parallel` flag:
```bash
chainsaw test --test-file test.yaml --parallel=N
```
Where `N` is the number of concurrent tests you want to run.

### Configuration
```yaml
# .chainsaw.yaml
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Configuration
metadata:
  name: configuration
spec:
  timeouts:
    assert: 90s
    error: 90s
  parallel: 10  # Number of parallel tests
  failFast: false
  forceTerminationGracePeriod: 5s
  delayBeforeCleanup: 3s
```

## Concurrency Management

### Namespace Isolation
Chainsaw automatically manages test isolation through:
- Unique namespace generation for each test
- Format: `chainsaw-<adjective>-<animal>` (e.g., chainsaw-wealthy-civet)
- Automatic cleanup after test completion

### Resource Management
- Each test runs in its own isolated namespace
- Resources are scoped to their respective namespaces
- Cleanup is handled per-test
- Timeouts and termination are managed independently

## Test Structure

### Example Test File
```yaml
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: scan-policy-test
spec:
  steps:
    - try:
      - script:
          content: |
            set -e
            nctl scan kubernetes -r path/to/resource.yaml -p path/to/policy.yaml
          check:
            ($error != null): true
            "(contains($stdout, 'Rule Results'))": true
    - finally:
        # Cleanup steps
```

### Parallel Test Considerations
1. Tests should be independent
2. Avoid shared resources between tests
3. Include proper cleanup in `finally` blocks
4. Use appropriate timeouts

## Go Integration

### Example Go Test Implementation
```go
package tests

import (
    "testing"
    "os/exec"
)

func TestParallelPolicyScan(t *testing.T) {
    tests := []struct {
        name     string
        testFile string
    }{
        {"BasicPolicyScan", "test/chainsaw/scan/basic_policy.yaml"},
        {"ComplexPolicyScan", "test/chainsaw/scan/complex_policy.yaml"},
        // Add more test cases
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            t.Parallel() // Enable parallel testing in Go

            cmd := exec.Command("chainsaw", "test",
                "--test-file", tt.testFile,
                "--parallel", "10")
            
            output, err := cmd.CombinedOutput()
            if err != nil {
                t.Errorf("Test failed: %v\nOutput: %s", err, output)
            }
        })
    }
}
```

### Output Validation
```go
var ExpectedOutputs = map[string][]string{
    "test-case-1": {
        `Rule Results\s*:\s*\(Fail:\s*1,\s*Warn:\s*0,\s*Pass:\s*0\)`,
        `Failed Rules Severity\s*:\s*\(Critical:\s*0,\s*High:\s*0,\s*Medium:\s*1\)`,
    },
}
```

## Best Practices

### Performance Optimization
1. Start with a small number of parallel tests (5-10)
2. Monitor cluster resource usage
3. Adjust parallel count based on:
   - Cluster capacity
   - Test complexity
   - Resource requirements

### Resource Management
1. Set appropriate timeouts:
   - `assertTimeout`: For validation checks
   - `cleanupTimeout`: For resource cleanup
   - `execTimeout`: For command execution

2. Configure cleanup delays:
   - `forceTerminationGracePeriod`: 5s (recommended)
   - `delayBeforeCleanup`: 3s (recommended)

### Error Handling
1. Implement proper error checks in test scripts
2. Use `finally` blocks for cleanup
3. Set `failFast: false` for parallel execution
4. Monitor test outputs and logs

### Cluster Considerations
1. Be cautious with cluster-scoped resources
2. Monitor API server load
3. Consider resource quotas
4. Watch for network policy impacts

## Troubleshooting

### Common Issues
1. Resource conflicts
   - Solution: Ensure proper namespace isolation
2. Timeout errors
   - Solution: Adjust timeout configurations
3. Cleanup failures
   - Solution: Implement robust finally blocks

### Debugging
1. Use `--verbose` flag for detailed logs
2. Check namespace creation/deletion
3. Monitor resource usage
4. Review test outputs carefully

## Conclusion
Chainsaw's parallel testing capabilities provide efficient test execution while maintaining isolation and concurrency safety. By following these guidelines and best practices, you can effectively implement parallel policy validation tests in your environment. 
