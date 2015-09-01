/**
 * Created by ap0ca1ip53 on 21/08/15.
 */

(function(){
    var lista=$("#OSList");
    var btcancelaros=lista.find('a.cancelarbt');

    btcancelaros.click(function(e){
        var self=$(this);

        if (confirm("Deseja cancelar a OS?")){
            self.parents("form").submit();
        } else {
            return false;
        }
    });
})();