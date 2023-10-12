# APP123 based deployment

APP123 is a Python/R soft
## Configuration 

Use shell

## Initial setup
setup only once:

```shell
./scripts/initial-setup.sh
```

## Updating configuration

To create and update application configuration use following scripts:

```shell
./scripts/run-one.sh 
./scripts/run-two.sh up --build app-config
```

Second line will update application properties files.

It's a good practice to run also:

```shell
./scripts/run-tree.sh 
```

## Running

To run the application use:

```shell
./scripts/run-app.sh --profile all up -d
```

To run only application dependencies (i.e. databases) run:

```shell
./scripts/run-app.sh --profile deps up -d
```

## Secrets

 * Add the key to the store:
   ```bash
    $ cd deployment
    $ git secret tell foo@wp.pl
   ```
 * Commit and push the change to a new branch.

Useful commands:
* `git secret 

## Links

### Local (http)

Available with local deployment from this repo.

#### Apps

- app1: http://localhost:8081/
- app2: http://localhost:8090/
- app3: http://localhost:8080/

#### Admin

## License
The GNU General Public License v3.0

