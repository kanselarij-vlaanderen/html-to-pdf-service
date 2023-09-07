"""
This is currently unused, but can be used in the future to facilitate
communication between this microservice and others via the db instead of
directly
"""
from string import Template

from escape_helpers import sparql_escape_uri, sparql_escape_string, sparql_escape_int, sparql_escape_datetime

from config import MU_APPLICATION_GRAPH
from lib.types import PhysicalFileResource, VirtualFileResource


def template_insert_file_query(
        virtual_file: VirtualFileResource,
        physical_file: PhysicalFileResource,
        graph: str = MU_APPLICATION_GRAPH
):
    """
    Construct a SPARQL query for inserting a file.
    :param file: dict containing properties for the virtual file
    :param physical_file: dict containing properties for the physical file
    :returns: string containing SPARQL query
    """
    query_template = Template("""
PREFIX mu: <http://mu.semte.ch/vocabularies/core/>
PREFIX nfo: <http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#>
PREFIX nie: <http://www.semanticdesktop.org/ontologies/2007/01/19/nie#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dbpedia: <http://dbpedia.org/ontology/>

INSERT DATA {
    GRAPH $graph {
        $uri a nfo:FileDataObject ;
            mu:uuid $uuid ;
            nfo:fileName $name ;
            dct:format $mimetype ;
            dct:created $created ;
            nfo:fileSize $size ;
            dbpedia:fileExtension $extension .
        $physical_uri a nfo:FileDataObject ;
            mu:uuid $physical_uuid ;
            nfo:fileName $physical_name ;
            dct:format $mimetype ;
            dct:created $created ;
            nfo:fileSize $size ;
            dbpedia:fileExtension $extension ;
            nie:dataSource $uri .
    }
}
""")
    return query_template.substitute(
        graph=sparql_escape_uri(graph),
        uri=sparql_escape_uri(virtual_file["uri"]),
        uuid=sparql_escape_string(virtual_file["uuid"]),
        name=sparql_escape_string(virtual_file["name"]),
        mimetype=sparql_escape_string(virtual_file["mime_type"]),
        created=sparql_escape_datetime(virtual_file["created"]),
        size=sparql_escape_int(virtual_file["size"]),
        extension=sparql_escape_string(virtual_file["extension"]),
        physical_uri=sparql_escape_uri(physical_file["uri"]),
        physical_uuid=sparql_escape_string(physical_file["uuid"]),
        physical_name=sparql_escape_string(physical_file["name"]))
