export default class Http {
    static server = 'http://localhost:5000';

    static async login(formVal) {
        let headers = new Headers();
		headers.append('Content-Type', 'application/json');
		headers.append('Accept', 'application/json');
		headers.append('Access-Control-Allow-Origin', this.server);
		headers.append('Access-Control-Allow-Credentials', 'true');
		headers.append('GET', 'POST', 'OPTIONS');

        const URL = Http.server + '/login';
        const response = await fetch(URL, {
            method: 'POST',
            headers: headers,
            body: `{
              "user":"${formVal.user}",
              "pwd":"${formVal.pwd}"
               }`,
          });
        return await response.json();
    }
    static async consulta(num){
        const URL = Http.server + '/consulta?num=' + num;
        const response = await fetch(URL);
        const res = await response.json();
        return res;
    }
}