
        const button=document.querySelector(".passReavealBtn");
        const pass = document.querySelector("#userpass");
        const pass1 = document.querySelector("#userpass1");
        let show = true;


        button.addEventListener('click' , ()=>{
            if (show){
                pass.type="text";
                if(pass1){
                pass1.type="text";
                }
                button.innerText="😑";
                show=false;
            }else{
                pass.type="password";
                if(pass1){
                pass1.type="password";
                }
                button.innerText="🙂";
                show=true;
            }
        });