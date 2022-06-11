# app
A simple Express web server that outputs "Hello world!" as a JSON message.

## Configuration
The following characteristics are configurable in the application through
environment variables. Create a `.env` file to control the configuration.

**IMPORTANT**: You MUST provide a `.env` file even if you do not override any of the default configuration values.

|Variable|Required|Default|Description|
|---|:-:|---|---|
|MESSAGE|F|"Hello world!"|Friendly message|
|PORT|F|3000|Server port|

## Usage

### Run
Launch the server. The npm package `forever` keeps the process alive.

```bash
npm start
```

### Status
The npm status script uses the `forever` package's `list` command to retrieve the status of the app.

```bash
npm run status
```

### Stop
Then npm stop script uses the `forever` package's `stopall` command can be used to stop the app.

```bash
npm run stop
```

### Test
Test the server.

```bash
npm test
```
