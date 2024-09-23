import { exec } from 'child_process';

function convert(stdout) {
    // console.log(stdout.split("\n"))
    let truc = []

    let list = stdout.split("\n");

    list.forEach(element => {
        // Splitter chaque élément par " : "
        let tmp = element.split(" : ");

        if (!tmp[1])
            return

        // console.log(tmp[1])

        // Corriger la structure pour un format JSON valide
        let correctedInput = tmp[1].replace(/\(/g, '[').replace(/\)/g, ']');

        try {
            // Parse la chaîne JSON corrigée
            let parsedArray = JSON.parse(correctedInput);

            // Transformer chaque élément du tableau en un objet
            let result = parsedArray.map(item => {
                return {
                    gen: tmp[0],
                    table: item[0],
                    score: item[1]
                };
            });

            // Ajouter les objets à truc.value
            truc.push(...result);
        } catch (error) {
            console.error("Erreur lors du parsing JSON:", error);
        }
    });

    return truc;
}

export default defineEventHandler(async (event) => {
    return new Promise((resolve, reject) => {
        exec('python3 ../main.py -n 5', (error, stdout, stderr) => {
            if (error) {
                reject({ error: error.message });
            } else if (stderr) {
                reject({ error: stderr });
            } else {
                let result = convert(stdout);

                resolve({ output: result });
            }
        });
    });
});
