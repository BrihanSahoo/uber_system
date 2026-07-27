import h3

class H3Service:
    
    """
    
    
    Converts geographic coordinates into H3 cells
    and retrieves neighboring cells.
    
    
    """
    
    RESOLUTION = 9
    @staticmethod
    def get_cell(self,latitude:float,longitude:float)->str:
        
        """
        
        
        Returns the H3 cell for a latitude/longitude.
        
        
        """
        
        return h3.latlng_to_cell(
            latitude,
            longitude,
            self.RESOLUTION  
        )
    
    @staticmethod
    def get_neighbor_cells(
        self,
        cell_id:str,
        radius:int
    )->list[str]:
        return list(
            h3.grid_disk(
                cell_id,
                radius
            )
        )
        