#!./paraview-5.11.1/bin/pvpython
# script-version: 2.0
# Catalyst state generated using paraview version 5.9.1
#### import the simple module from the paraview
import paraview
from paraview.simple import *
import os

def formatCT(ct):
    max = 9
    if(len(ct) == max):
        return ct
    ct_id = ""
    for i in range(0,(max-len(ct))):
        ct_id = ct_id + "0"
    ct_id = ct_id + ct
    return ct_id


def run_postproc(output_path, ct):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1254, 643]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.OrientationAxesVisibility = 0
    renderView1.CenterOfRotation = [13.5, 6.0, 5.1000001430511475]
    renderView1.UseToneMapping = 1
    renderView1.UseAmbientOcclusion = 1
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [13.5, 6.0, 27.373379549778527]
    renderView1.CameraFocalPoint = [13.5, 6.0, -25.74375922742822]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 13.74772713689472
    renderView1.BackEnd = 'OSPRay raycaster'
    renderView1.OSPRayMaterialLibrary = materialLibrary1
    
    SetActiveView(None)
    
    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------
    
    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    layout1.SetSize(1254, 643)
    
    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------


    # create a new 'VisItChomboReader'
    f_name = output_path+'/ns_output_ct.'+formatCT(ct)+'.hdf5'
    if not os.path.isfile(f_name):
        print("Can't find HDF5 file: "+f_name)
        exit(1)

    ns_output_ct = VisItChomboReader(registrationName='ns_output_ct.*', FileName=[f_name])
    ns_output_ct.MeshStatus = ['Mesh']
    ns_output_ct.PointArrayStatus = ['Mach', 'density', 'ib_marker', 'isoQ', 'presscorrec', 'pressure', 'temperature', 'turbvisc', 'u', 'v', 'viscosity', 'vortmag', 'vortx', 'vorty', 'vortz', 'w']

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=ns_output_ct)
    calculator1.ResultArrayName = 'velocidade'
    calculator1.Function = 'u*iHat+v*jHat+w*kHat'

    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=calculator1)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [13.500000000000005, 6.000000000000005, 4.945]
    slice1.SliceType.Normal = [0.0, 0.0, 1.0]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [13.500000000000005, 6.000000000000005, 5.099999999999999]

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from slice1
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # get 2D transfer function for 'Mach'
    machTF2D = GetTransferFunction2D('Mach')

    # get color transfer function/color map for 'Mach'
    machLUT = GetColorTransferFunction('Mach')
    machLUT.TransferFunction2D = machTF2D
    machLUT.RGBPoints = [0.00041561559837389377, 0.231373, 0.298039, 0.752941, 0.28215097106958137, 0.865003, 0.865003, 0.865003, 0.5638863265407889, 0.705882, 0.0156863, 0.14902]
    machLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = ['POINTS', 'Mach']
    slice1Display.LookupTable = machLUT
    slice1Display.SelectTCoordArray = 'None'
    slice1Display.SelectNormalArray = 'None'
    slice1Display.SelectTangentArray = 'None'
    slice1Display.OSPRayScaleArray = 'Mach'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'velocidade'
    slice1Display.ScaleFactor = 2.4000000000000004
    slice1Display.SelectScaleArray = 'Mach'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'Mach'
    slice1Display.GaussianRadius = 0.12
    slice1Display.SetScaleArray = ['POINTS', 'Mach']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'Mach']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.SelectInputVectors = ['POINTS', 'velocidade']
    slice1Display.WriteLog = ''

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for machLUT in view renderView1
    machLUTColorBar = GetScalarBar(machLUT, renderView1)
    machLUTColorBar.Orientation = 'Horizontal'
    machLUTColorBar.WindowLocation = 'Any Location'
    machLUTColorBar.Position = [0.32141945773524716, 0.09776049766718507]
    machLUTColorBar.Title = 'Mach'
    machLUTColorBar.ComponentTitle = ''
    machLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    machLUTColorBar.TitleFontSize = 20
    machLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    machLUTColorBar.LabelFontSize = 18
    machLUTColorBar.ScalarBarLength = 0.3300000000000003
    machLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    machLUTColorBar.Visibility = 1

    # show color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get opacity transfer function/opacity map for 'Mach'
    machPWF = GetOpacityTransferFunction('Mach')
    machPWF.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]
    machPWF.ScalarRangeInitialized = 1

    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------

    # create extractor
    pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
    # trace defaults for the extractor.
    pNG1.Trigger = 'TimeStep'

    # init the 'PNG' selected for 'Writer'
    pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
    pNG1.Writer.ImageResolution = [1254, 643]
    pNG1.Writer.TransparentBackground = 1
    pNG1.Writer.Format = 'PNG'
    pNG1.Writer.PhiResolution = 183

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG1)
    # ----------------------------------------------------------------

    # ------------------------------------------------------------------------------
    # Catalyst options
    from paraview import catalyst
    options = catalyst.Options()
    options.ExtractsOutputDirectory = 'datasetsanother'
    options.GlobalTrigger = 'TimeStep'
    options.CatalystLiveTrigger = 'TimeStep'

    # init the 'TimeValue' selected for 'GlobalTrigger'
    # options.GlobalTrigger.Length = 1.0
    SaveExtractsUsingCatalystOptions(options)

