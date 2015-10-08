### TDD demo

Just some common tools are using here:

1.  `virtualenv` is using as python version swticher
2.  `pip` as package manager
3.  `nosetests` as python test runner
4.  `unittest` as test framework

#### Get started

```sh
$ pip install virtualenv
```

```sh
$ virtualenv tdd #create a new env, named `tdd`
$ source tdd/bin/activate #activate it
```

#### Dependencies management

put all your requirements in file `requirements.txt`, and then

```sh
$ pip install -r requirements.txt
```

To run tests:

```sh
$ nosetests 
```