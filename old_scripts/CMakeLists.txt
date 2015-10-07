cmake_minimum_required(VERSION 2.8)

PROJECT(Thesis NONE)

INCLUDE(UseLATEX.cmake)
FILE(GLOB_RECURSE contents_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} content/*.tex)
FILE(GLOB awk_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} cmake_latexscripts/*.awk)
FILE(GLOB dot_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} content/pictures/*.dot)

FOREACH(dot ${dot_files})
    GET_FILENAME_COMPONENT(fname ${dot} NAME_WE)
    GET_FILENAME_COMPONENT(fpath ${dot} PATH)
    SET(depend "${fpath}/${fname}")
    SET(depend "${depend}.png")
    ADD_CUSTOM_COMMAND(
        OUTPUT ${depend}
        COMMAND dot 
        ARGS -Tpng ${CMAKE_CURRENT_SOURCE_DIR}/${dot} -o${CMAKE_CURRENT_BINARY_DIR}/${depend})
    LIST(APPEND depends ${depend})
ENDFOREACH(dot)


ADD_LATEX_DOCUMENT(main.tex
    IMAGE_DIRS content/pictures
    INPUTS preamble.tex glossary.tex appendix.tex ${contents_files} ${awk_files}
    BIBFILES bibtex_timo.bib bibtex_kevin.bib
    USE_INDEX
    USE_GLOSSARY
    #    FILTER_OUTPUT
    DEPENDS ${depends}
    )


ADD_CUSTOM_TARGET(dropbox
    dropbox_uploader upload main.pdf Public/thesis.pdf
    )

ADD_DEPENDENCIES(dropbox pdf)
