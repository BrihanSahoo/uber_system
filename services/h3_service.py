import h3

class H3Service:
    
    
    @staticmethod
    def get_cell(latitude:float,longitude:float)->str:
        
        return h3.latlng_to_cell(
            latitude,
            longitude,
            9   
        )
    
    @staticmethod
    def get_neighbor_cells(
        cell_id:str,
        radius:int
    )->list[str]:
        return list(
            h3.grid_disk(
                cell_id,
                radius
            )
        )
        