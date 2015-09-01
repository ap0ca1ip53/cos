/**
 * Created by ap0ca1ip53 on 21/08/15.
 */

(function(){
    var lista=$("#instalacaoList");
    var deletebt=lista.find('a.apagarbt');

    deletebt.click(function(e){
        var self=$(this);

        if (confirm("Deseja excluir o registro?")){
            self.parents("form").submit();
        } else {
            return false;
        }
    });
})();