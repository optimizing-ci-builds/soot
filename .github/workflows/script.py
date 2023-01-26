name: Soot CI
'on':
  push: null
  pull_request: null
jobs:
  BuildAndTest:
    name: Build and Test with java ${{ matrix.java_version }}
    runs-on: ubuntu-latest
    strategy:
      matrix:
        java_version: '8'
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Use Java ${{ matrix.java_version }}
      uses: actions/setup-java@v1
      with:
        java-version: ${{ matrix.java_version }}
    - name: Build and test Java ${{ matrix.java_version }}
      run: 'mvn -B clean test -PJava${{ matrix.java_version }}

        '
