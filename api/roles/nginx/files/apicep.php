<?php

    $endereco = (object) [
        'cep' => '', 
        'logradouro' => '',  
        'bairro' => '', 
        'uf' => '',
        'ibge' => ''
    ];

    if ( isset ($_POST['cep'])){
    
        $cep = $_POST['cep'];
        
        // Acha tudo que não for número e substitui por nada '' e adiciona o valor a variavel $cep
        $cep = preg_replace('/[^0-9]/', '',$cep);

        // Verifica se a expressão regular é verdadeira. 
        if (preg_match('/^[0-9]{5}-?[0-9]{3}$/',$cep)){

            $url = "https://viacep.com.br/ws/{$cep}/json/";


            $endereco = json_decode(file_get_contents($url));

        } else {
            $endereco->cep = 'CEP Inválido!';
        }

    }

?>