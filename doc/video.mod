<!-- Setting up a quick mod file for reference -->



<!--                    LONG NAME: Video                            -->
<!ENTITY % video.content
                       "((%desc;)?,
                         (%longdescref;)?,
                         (%fallback;)?,
                         (%video-poster;)?,
                         (%media-source;)*,
                         (%media-track;)*,
                         (%foreign;)*)"
>
<!ENTITY % video.attributes
              "autoplay
                          (true |
                           false |
                           -dita-use-conref-target)
                                    #IMPLIED
               controls
                          (true |
                           false |
                           -dita-use-conref-target)
                                    #IMPLIED
               loop
                          (true |
                           false |
                           -dita-use-conref-target)
                                    #IMPLIED
               muted
                          (true |
                           false |
                           -dita-use-conref-target)
                                    #IMPLIED
               href
                          CDATA
                                    #IMPLIED
               keyref
                          CDATA
                                    #IMPLIED
               format
                          CDATA
                                    #IMPLIED
               scope
                          (external |
                           local |
                           peer |
                           -dita-use-conref-target)
                                    #IMPLIED
               height
                          NMTOKEN
                                    #IMPLIED
               width
                          NMTOKEN
                                    #IMPLIED
               tabindex
                          NMTOKEN
                                    #IMPLIED
               %univ-atts;"
>
<!ELEMENT  video %video.content;>
<!ATTLIST  video %video.attributes;>

