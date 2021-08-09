<?php
    include_once ('apicep.php');
?>

<!doctype html>
<html lang="en">
  <head>
    <title>API via CEP</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  </head>
  <body>
  
        <!-- First Container -->
        <div class="container-fluid bg-1 text-center">
            <h1 class="margin"></h1>
            <h5 class="margin">Digite um cep para obter as informações</h5>
        </div>

        <!-- Second Container -->
        <form action="." method="POST">
            <div class="container">
                <div class="row justify-content-md-center">
                    <div class="col-md-5">
                        <input class="form-control form-control-sm" type="text" name="cep" value="<?php echo $endereco->cep?>" placeholder="Digite um cep...">
                        <button type="submit" class="btn btn-primary btn-sm btn-block">Enviar</button>
                        <input class="form-control form-control-sm" type="text" name="rua" value="<?php echo $endereco->logradouro?>" placeholder="Rua">
                        <input class="form-control form-control-sm" type="text" name="bairro" value="<?php echo $endereco->bairro?>" placeholder="Bairro">
                        <input class="form-control form-control-sm" type="text" name="uf" value="<?php echo $endereco->uf?>" placeholder="UF">
                        <input class="form-control form-control-sm" type="text" name="ibge" value="<?php echo $endereco->ibge?>" placeholder="Código do IBGE">
                    </div>
                </div>   
            </div>
        </form>
        

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>