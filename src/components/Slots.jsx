
function Slots({type="th"}){
    const slots = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'A2' ,'B2' ,'C2', 'D2', 'E2', 'F2', 'G2', ''
    ] 

    if(type=="th"){
        return(
            <div class="slots">
                <p>THEORY ONLY SLOTS</p>
            </div>
        )}
        else if(type=="eth"){
            return(
                <div class="slots">
                    <p>LAB ALSO</p>
                </div>
            )
        }
}

export default Slots;