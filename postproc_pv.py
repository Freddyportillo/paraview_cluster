#!./paraview-5.11.1/bin/pvpython
# script-version: 2.0
# Catalyst state generated using paraview version 5.9.1
#### import the simple module from the paraview
import paraview
from paraview.simple import *
import os


def run_postproc(output_path, result_path, ct):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------
    # file_id = '50m_40s' #output_path[len(output_path)-14:]
    splt = output_path.split('/')
    file_id = splt[len(splt)-2]+'-'+splt[len(splt)-1]
    
    # get the material library
    materialLibrary1 = GetMaterialLibrary()
############################################################################################
#           MACH
############################################################################################
    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1254, 643]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.OrientationAxesVisibility = 0
    renderView1.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [13.5, 6.0, 27.436913333807976]
    renderView1.CameraFocalPoint = [13.5, 6.0, -24.400106077512277]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 13.41640786499874
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
    # f_name = output_path+'/ns_output_ct.'+formatCT(ct)+'.hdf5'
    # if not os.path.isfile(f_name):
    #     print("Can't find HDF5 file: "+f_name)
    #     exit(1)
    f_name = output_path+'/'+ct

    ns_output_ct = VisItChomboReader(registrationName='ns_output_ct.*', FileName=[f_name])
    ns_output_ct.MeshStatus = ['Mesh']
    ns_output_ct.PointArrayStatus = ['Mach', 'density', 'ib_marker', 'isoQ', 'presscorrec', 'pressure', 'temperature', 'turbvisc', 'u', 'v', 'viscosity', 'vortmag', 'vortx', 'vorty', 'vortz', 'w']

    # create a new 'XML Partitioned Polydata Reader'
    ibm_fim_001_000000000pvtp = XMLPartitionedPolydataReader(registrationName='ibm_fim_001_000000000.pvtp*', FileName=[output_path+'/IB/pvtp/ibm_fim_001_000000000.pvtp'])
    ibm_fim_001_000000000pvtp.CellArrayStatus = ['Area', 'Delta_s', 'Force', 'Normals', 'Velocity']
    ibm_fim_001_000000000pvtp.TimeArray = 'None'

    # create a new 'XML Partitioned Polydata Reader'
    ibm_fim_002_000000000pvtp = XMLPartitionedPolydataReader(registrationName='ibm_fim_002_000000000.pvtp*', FileName=[output_path+'/IB/pvtp/ibm_fim_002_000000000.pvtp'])
    ibm_fim_002_000000000pvtp.CellArrayStatus = ['Area', 'Delta_s', 'Force', 'Normals', 'Velocity']
    ibm_fim_002_000000000pvtp.TimeArray = 'None'

    # create a new 'XML Partitioned Polydata Reader'
    ibm_fim_003_000000000pvtp = XMLPartitionedPolydataReader(registrationName='ibm_fim_003_000000000.pvtp*', FileName=[output_path+'/IB/pvtp/ibm_fim_003_000000000.pvtp'])
    ibm_fim_003_000000000pvtp.CellArrayStatus = ['Area', 'Delta_s', 'Force', 'Normals', 'Velocity']
    ibm_fim_003_000000000pvtp.TimeArray = 'None'

    # show data from ibm_fim_002_000000000pvtp
    ibm_fim_002_000000000pvtpDisplay = Show(ibm_fim_002_000000000pvtp, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_002_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_002_000000000pvtpDisplay.AmbientColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_002_000000000pvtpDisplay.DiffuseColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_002_000000000pvtpDisplay.ScaleFactor = 0.09450006484985352
    ibm_fim_002_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_002_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GaussianRadius = 0.004725003242492676
    ibm_fim_002_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_002_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_001_000000000pvtp
    ibm_fim_001_000000000pvtpDisplay = Show(ibm_fim_001_000000000pvtp, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_001_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_001_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_001_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_001_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_001_000000000pvtpDisplay.ScaleFactor = 1.8512276996023616
    ibm_fim_001_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_001_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GaussianRadius = 0.09256138498011808
    ibm_fim_001_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_001_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_003_000000000pvtp
    ibm_fim_003_000000000pvtpDisplay = Show(ibm_fim_003_000000000pvtp, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_003_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_003_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_003_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_003_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_003_000000000pvtpDisplay.ScaleFactor = 0.4997869968414307
    ibm_fim_003_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_003_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GaussianRadius = 0.024989349842071535
    ibm_fim_003_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_003_000000000pvtpDisplay.WriteLog = ''
    
    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=ns_output_ct)
    calculator1.ResultArrayName = 'velocity'
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
    
    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=slice1)
    threshold1.Scalars = ['POINTS', 'ib_marker']
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 1.0
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from mach
    # threshold1Display = Show(mach, renderView1, 'GeometryRepresentation')
    # show data from threshold1
    threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')
    # get 2D transfer function for 'Mach'
    machTF2D = GetTransferFunction2D('Mach')

    # get color transfer function/color map for 'Mach'
    machLUT = GetColorTransferFunction('Mach')
    machLUT.TransferFunction2D = machTF2D
    machLUT.RGBPoints = [0.00041561559837389377, 0.231373, 0.298039, 0.752941, 0.28215097106958137, 0.865003, 0.865003, 0.865003, 0.5638863265407889, 0.705882, 0.0156863, 0.14902]
    machLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'Mach']
    threshold1Display.LookupTable = machLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'Mach'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'velocity'
    threshold1Display.ScaleFactor = 2.4000000000000004
    threshold1Display.SelectScaleArray = 'Mach'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'Mach'
    threshold1Display.GaussianRadius = 0.12
    threshold1Display.SetScaleArray = ['POINTS', 'Mach']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'Mach']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.SelectInputVectors = ['POINTS', 'velocity']
    threshold1Display.WriteLog = ''
    threshold1Display.RescaleTransferFunctionToDataRange(False, True)


    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for machLUT in view renderView1
    machLUTColorBar = GetScalarBar(machLUT, renderView1)
    machLUTColorBar.Orientation = 'Horizontal'
    machLUTColorBar.WindowLocation = 'Any Location'
    machLUTColorBar.Position = [0.32, 0.12]
    machLUTColorBar.Title = 'Mach'
    machLUTColorBar.ComponentTitle = ''
    machLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    machLUTColorBar.TitleFontSize = 22
    machLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    machLUTColorBar.LabelFontSize = 18
    machLUTColorBar.ScalarBarLength = 0.32999999999999985
    machLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    machLUTColorBar.Visibility = 1

    # show color legend
    threshold1Display.SetScalarBarVisibility(renderView1, True)

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
    pNG1.Writer.FileName = 'mach_'+file_id+'.png'
    pNG1.Writer.ImageResolution = [1254, 643]
    pNG1.Writer.TransparentBackground = 1
    pNG1.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG1)
    # ----------------------------------------------------------------
############################################################################################
#           PRESSURE
############################################################################################


    # Create a new 'Render View'
    renderView2 = CreateView('RenderView')
    renderView2.ViewSize = [1254, 643]
    renderView2.AxesGrid = 'GridAxes3DActor'
    renderView2.OrientationAxesVisibility = 0
    renderView2.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView2.StereoType = 'Crystal Eyes'
    renderView2.CameraPosition = [13.5, 6.0, 27.436913333807976]
    renderView2.CameraFocalPoint = [13.5, 6.0, -24.400106077512277]
    renderView2.CameraFocalDisk = 1.0
    renderView2.CameraParallelScale = 13.41640786499874
    renderView2.BackEnd = 'OSPRay raycaster'
    renderView2.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView2)
    layout1.SetSize(1254, 643)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView2)
    # ----------------------------------------------------------------

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
    
    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=slice1)
    threshold1.Scalars = ['POINTS', 'ib_marker']
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 1.0
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from pressure
    # threshold1Display = Show(pressure, renderView2, 'GeometryRepresentation')
    threshold1Display = Show(threshold1, renderView2, 'UnstructuredGridRepresentation')
    
    # get 2D transfer function for 'pressure'
    pressureTF2D = GetTransferFunction2D('pressure')
    
    # get color transfer function/color map for 'pressure'
    pressureLUT = GetColorTransferFunction('pressure')
    pressureLUT.TransferFunction2D = pressureTF2D
    pressureLUT.RGBPoints = [279745.6502463703, 0.231373, 0.298039, 0.752941, 291750.69232371537, 0.865003, 0.865003, 0.865003, 303755.73440106044, 0.705882, 0.0156863, 0.14902]
    pressureLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'pressure']
    threshold1Display.LookupTable = pressureLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'Mach'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'velocity'
    threshold1Display.ScaleFactor = 2.4000000000000004
    threshold1Display.SelectScaleArray = 'Mach'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'Mach'
    threshold1Display.GaussianRadius = 0.12
    threshold1Display.SetScaleArray = ['POINTS', 'Mach']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'Mach']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.SelectInputVectors = ['POINTS', 'velocity']
    threshold1Display.WriteLog = ''
    threshold1Display.RescaleTransferFunctionToDataRange(False, True)
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [0.00041561559837389377, 0.0, 0.5, 0.0, 0.5638863265407889, 1.0, 0.5, 0.0]
    
    # setup the color legend parameters for each legend in this view
    
    # get color legend/bar for pressureLUT in view renderView1
    pressureLUTColorBar = GetScalarBar(pressureLUT, renderView2)
    pressureLUTColorBar.Orientation = 'Horizontal'
    pressureLUTColorBar.WindowLocation = 'Any Location'
    pressureLUTColorBar.Position = [0.32, 0.12]
    pressureLUTColorBar.Title = 'Pressão [Pa]'
    pressureLUTColorBar.ComponentTitle = ''
    pressureLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    pressureLUTColorBar.TitleFontSize = 20
    pressureLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    pressureLUTColorBar.LabelFontSize = 18
    pressureLUTColorBar.ScalarBarLength = 0.32999999999999957
    
    # set color bar visibility
    pressureLUTColorBar.Visibility = 1
    
    # show color legend
    threshold1Display.SetScalarBarVisibility(renderView2, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # get opacity transfer function/opacity map for 'pressure'
    pressurePWF = GetOpacityTransferFunction('pressure')
    pressurePWF.Points = [279745.6502463703, 0.0, 0.5, 0.0, 303755.73440106044, 1.0, 0.5, 0.0]
    pressurePWF.ScalarRangeInitialized = 1
    
        # show data from ibm_fim_002_000000000pvtp
    ibm_fim_002_000000000pvtpDisplay = Show(ibm_fim_002_000000000pvtp, renderView2, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_002_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_002_000000000pvtpDisplay.AmbientColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_002_000000000pvtpDisplay.DiffuseColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_002_000000000pvtpDisplay.ScaleFactor = 0.09450006484985352
    ibm_fim_002_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_002_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GaussianRadius = 0.004725003242492676
    ibm_fim_002_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_002_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_001_000000000pvtp
    ibm_fim_001_000000000pvtpDisplay = Show(ibm_fim_001_000000000pvtp, renderView2, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_001_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_001_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_001_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_001_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_001_000000000pvtpDisplay.ScaleFactor = 1.8512276996023616
    ibm_fim_001_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_001_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GaussianRadius = 0.09256138498011808
    ibm_fim_001_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_001_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_003_000000000pvtp
    ibm_fim_003_000000000pvtpDisplay = Show(ibm_fim_003_000000000pvtp, renderView2, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_003_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_003_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_003_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_003_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_003_000000000pvtpDisplay.ScaleFactor = 0.4997869968414307
    ibm_fim_003_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_003_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GaussianRadius = 0.024989349842071535
    ibm_fim_003_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_003_000000000pvtpDisplay.WriteLog = ''
    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------
    
    # create extractor
    pNG2 = CreateExtractor('PNG', renderView2, registrationName='PNG2')
    # trace defaults for the extractor.
    pNG2.Trigger = 'TimeStep'
    
    # init the 'PNG' selected for 'Writer'
    pNG2.Writer.FileName = 'pressure_'+file_id+'.png'
    pNG2.Writer.ImageResolution = [1254, 643]
    pNG2.Writer.TransparentBackground = 1
    pNG2.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG2)

############################################################################################
#           velocity U
############################################################################################
# Create a new 'Render View'
    renderView3 = CreateView('RenderView')
    renderView3.ViewSize = [1254, 643]
    renderView3.AxesGrid = 'GridAxes3DActor'
    renderView3.OrientationAxesVisibility = 0
    renderView3.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView3.UseToneMapping = 1
    renderView3.Exposure = 2.2
    renderView3.StereoType = 'Crystal Eyes'
    renderView3.CameraPosition = [13.5, 6.0, 27.436913333807976]
    renderView3.CameraFocalPoint = [13.5, 6.0, -24.400106077512277]
    renderView3.CameraFocalDisk = 1.0
    renderView3.CameraParallelScale = 13.41640786499874
    renderView3.BackEnd = 'OSPRay raycaster'
    renderView3.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView3)
    layout1.SetSize(1254, 643)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView3)
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

    # create a new 'VisItChomboReader'
    ns_output = VisItChomboReader(registrationName='ns_output_ct.000168000.hdf5', FileName=['/media/alejandro/HD_int_1TB/UFCC/outs/mmvillar/ib_ml/out_smagL5piso/ns_output_ct.000168000.hdf5'])
    ns_output.MeshStatus = ['Mesh']
    ns_output.PointArrayStatus = ['Mach', 'density', 'ib_marker', 'isoQ', 'presscorrec', 'pressure', 'temperature', 'turbvisc', 'u', 'v', 'viscosity', 'vortmag', 'vortx', 'vorty', 'vortz', 'w']

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
    
    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=slice1)
    threshold1.Scalars = ['POINTS', 'ib_marker']
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 1.0
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from pressure
    # threshold1Display = Show(pressure, renderView2, 'GeometryRepresentation')
    threshold1Display = Show(threshold1, renderView3, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'u'
    uTF2D = GetTransferFunction2D('u')

    # get color transfer function/color map for 'u'
    uLUT = GetColorTransferFunction('u')
    uLUT.TransferFunction2D = uTF2D
    uLUT.RGBPoints = [-50.779897689513106, 0.231373, 0.298039, 0.752941, 47.07150039761133, 0.865003, 0.865003, 0.865003, 144.92289848473575, 0.705882, 0.0156863, 0.14902]
    uLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'u']
    threshold1Display.LookupTable = uLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'Mach'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'None'
    threshold1Display.ScaleFactor = 2.4000000000000012
    threshold1Display.SelectScaleArray = 'Mach'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'Mach'
    threshold1Display.GaussianRadius = 0.12000000000000005
    threshold1Display.SetScaleArray = ['POINTS', 'Mach']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'Mach']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.SelectInputVectors = [None, '']
    threshold1Display.WriteLog = ''
    threshold1Display.RescaleTransferFunctionToDataRange(False, True)

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [0.00041561559837389263, 0.0, 0.5, 0.0, 0.5638863265407886, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [0.00041561559837389263, 0.0, 0.5, 0.0, 0.5638863265407886, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for uLUT in view renderView3
    uLUTColorBar = GetScalarBar(uLUT, renderView3)
    uLUTColorBar.Orientation = 'Horizontal'
    uLUTColorBar.WindowLocation = 'Any Location'
    uLUTColorBar.Position = [0.32, 0.12]
    uLUTColorBar.Title = 'u [m/s]'
    uLUTColorBar.ComponentTitle = ''
    uLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    uLUTColorBar.TitleFontSize = 20
    uLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    uLUTColorBar.LabelFontSize = 18
    uLUTColorBar.ScalarBarLength = 0.33000000000000035
    uLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    uLUTColorBar.Visibility = 1

    # show color legend
    threshold1Display.SetScalarBarVisibility(renderView3, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get opacity transfer function/opacity map for 'u'
    uPWF = GetOpacityTransferFunction('u')
    uPWF.Points = [-50.779897689513106, 0.0, 0.5, 0.0, 144.92289848473575, 1.0, 0.5, 0.0]
    uPWF.ScalarRangeInitialized = 1

    # show data from ibm_fim_002_000000000pvtp
    ibm_fim_002_000000000pvtpDisplay = Show(ibm_fim_002_000000000pvtp, renderView3, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_002_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_002_000000000pvtpDisplay.AmbientColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_002_000000000pvtpDisplay.DiffuseColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_002_000000000pvtpDisplay.ScaleFactor = 0.09450006484985352
    ibm_fim_002_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_002_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GaussianRadius = 0.004725003242492676
    ibm_fim_002_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_002_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_001_000000000pvtp
    ibm_fim_001_000000000pvtpDisplay = Show(ibm_fim_001_000000000pvtp, renderView3, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_001_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_001_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_001_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_001_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_001_000000000pvtpDisplay.ScaleFactor = 1.8512276996023616
    ibm_fim_001_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_001_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GaussianRadius = 0.09256138498011808
    ibm_fim_001_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_001_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_003_000000000pvtp
    ibm_fim_003_000000000pvtpDisplay = Show(ibm_fim_003_000000000pvtp, renderView3, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_003_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_003_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_003_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_003_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_003_000000000pvtpDisplay.ScaleFactor = 0.4997869968414307
    ibm_fim_003_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_003_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GaussianRadius = 0.024989349842071535
    ibm_fim_003_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_003_000000000pvtpDisplay.WriteLog = ''
    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------

    # create extractor
    pNG3 = CreateExtractor('PNG', renderView3, registrationName='PNG3')
    # trace defaults for the extractor.
    pNG3.Trigger = 'TimeValue'

    # init the 'PNG' selected for 'Writer'
    pNG3.Writer.FileName = 'u_vel_'+file_id+'.png'
    pNG3.Writer.ImageResolution = [1254, 643]
    pNG3.Writer.TransparentBackground = 1
    pNG3.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG3)


############################################################################################
#           velocity V
############################################################################################

    # Create a new 'Render View'
    renderView4 = CreateView('RenderView')
    renderView4.ViewSize = [1254, 643]
    renderView4.AxesGrid = 'GridAxes3DActor'
    renderView4.OrientationAxesVisibility = 0
    renderView4.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView4.UseToneMapping = 1
    renderView4.Exposure = 2.2
    renderView4.StereoType = 'Crystal Eyes'
    renderView4.CameraPosition = [13.5, 6.0, 27.436913333807976]
    renderView4.CameraFocalPoint = [13.5, 6.0, -24.400106077512277]
    renderView4.CameraFocalDisk = 1.0
    renderView4.CameraParallelScale = 13.41640786499874
    renderView4.BackEnd = 'OSPRay raycaster'
    renderView4.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView4)
    layout1.SetSize(1254, 643)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView4)
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ---------------------------------------------------------------
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
    
    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=slice1)
    threshold1.Scalars = ['POINTS', 'ib_marker']
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 1.0
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from pressure
    # threshold1Display = Show(pressure, renderView2, 'GeometryRepresentation')
    threshold1Display = Show(threshold1, renderView4, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'v'
    vTF2D = GetTransferFunction2D('v')

    # get color transfer function/color map for 'v'
    vLUT = GetColorTransferFunction('v')
    vLUT.TransferFunction2D = vTF2D
    vLUT.RGBPoints = [-299.12179020725245, 0.231373, 0.298039, 0.752941, -105.43366648635393, 0.865003, 0.865003, 0.865003, 88.25445723454459, 0.705882, 0.0156863, 0.14902]
    vLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'v']
    threshold1Display.LookupTable = vLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'Mach'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'None'
    threshold1Display.ScaleFactor = 2.4000000000000012
    threshold1Display.SelectScaleArray = 'Mach'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'Mach'
    threshold1Display.GaussianRadius = 0.12000000000000005
    threshold1Display.SetScaleArray = ['POINTS', 'Mach']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'Mach']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.SelectInputVectors = [None, '']
    threshold1Display.WriteLog = ''
    threshold1Display.RescaleTransferFunctionToDataRange(False, True)

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [0.00041561559837389263, 0.0, 0.5, 0.0, 0.5638863265407886, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [0.00041561559837389263, 0.0, 0.5, 0.0, 0.5638863265407886, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for vLUT in view renderView4
    vLUTColorBar = GetScalarBar(vLUT, renderView4)
    vLUTColorBar.Orientation = 'Horizontal'
    vLUTColorBar.WindowLocation = 'Any Location'
    vLUTColorBar.Position = [0.32, 0.12]
    vLUTColorBar.Title = 'v [m/s]'
    vLUTColorBar.ComponentTitle = ''
    vLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    vLUTColorBar.TitleFontSize = 20
    vLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    vLUTColorBar.LabelFontSize = 18
    vLUTColorBar.ScalarBarLength = 0.3300000000000007
    vLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    vLUTColorBar.Visibility = 1

    # show color legend
    threshold1Display.SetScalarBarVisibility(renderView4, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get opacity transfer function/opacity map for 'v'
    vPWF = GetOpacityTransferFunction('v')
    vPWF.Points = [-299.12179020725245, 0.0, 0.5, 0.0, 88.25445723454459, 1.0, 0.5, 0.0]
    vPWF.ScalarRangeInitialized = 1

    # show data from ibm_fim_002_000000000pvtp
    ibm_fim_002_000000000pvtpDisplay = Show(ibm_fim_002_000000000pvtp, renderView4, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_002_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_002_000000000pvtpDisplay.AmbientColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_002_000000000pvtpDisplay.DiffuseColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_002_000000000pvtpDisplay.ScaleFactor = 0.09450006484985352
    ibm_fim_002_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_002_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GaussianRadius = 0.004725003242492676
    ibm_fim_002_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_002_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_001_000000000pvtp
    ibm_fim_001_000000000pvtpDisplay = Show(ibm_fim_001_000000000pvtp, renderView4, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_001_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_001_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_001_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_001_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_001_000000000pvtpDisplay.ScaleFactor = 1.8512276996023616
    ibm_fim_001_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_001_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GaussianRadius = 0.09256138498011808
    ibm_fim_001_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_001_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_003_000000000pvtp
    ibm_fim_003_000000000pvtpDisplay = Show(ibm_fim_003_000000000pvtp, renderView4, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_003_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_003_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_003_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_003_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_003_000000000pvtpDisplay.ScaleFactor = 0.4997869968414307
    ibm_fim_003_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_003_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GaussianRadius = 0.024989349842071535
    ibm_fim_003_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_003_000000000pvtpDisplay.WriteLog = ''
    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------

    # create extractor
    pNG4 = CreateExtractor('PNG', renderView4, registrationName='PNG4')
    # trace defaults for the extractor.
    pNG4.Trigger = 'TimeValue'

    # init the 'PNG' selected for 'Writer'
    pNG4.Writer.FileName = 'v_vel_'+file_id+'.png'
    pNG4.Writer.ImageResolution = [1254, 643]
    pNG4.Writer.TransparentBackground = 1
    pNG4.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG4)


############################################################################################
#           TEMPERATURE
############################################################################################

    # Create a new 'Render View'
    renderView5 = CreateView('RenderView')
    renderView5.ViewSize = [1254, 643]
    renderView5.AxesGrid = 'GridAxes3DActor'
    renderView5.OrientationAxesVisibility = 0
    renderView5.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView5.UseToneMapping = 1
    renderView5.Exposure = 2.2
    renderView5.StereoType = 'Crystal Eyes'
    renderView5.CameraPosition = [13.387304411089747, 6.0, 27.436631001770568]
    renderView5.CameraFocalPoint = [13.647033466856255, 6.0, -24.399737720075517]
    renderView5.CameraFocalDisk = 1.0
    renderView5.CameraParallelScale = 13.41640786499874
    renderView5.BackEnd = 'OSPRay raycaster'
    renderView5.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView5)
    layout1.SetSize(1254, 643)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView5)

# ----------------------------------------------------------------
    # setup the data processing pipelines
    # ---------------------------------------------------------------
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
    
    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=slice1)
    threshold1.Scalars = ['POINTS', 'ib_marker']
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 1.0
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from pressure
    # threshold1Display = Show(pressure, renderView2, 'GeometryRepresentation')
    threshold1Display = Show(threshold1, renderView5, 'UnstructuredGridRepresentation') 
    # ------------------------------------------------------------------------------

    # show data from ibm_fim_002_000000000pvtp
    ibm_fim_002_000000000pvtpDisplay = Show(ibm_fim_002_000000000pvtp, renderView5, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_002_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_002_000000000pvtpDisplay.AmbientColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_002_000000000pvtpDisplay.DiffuseColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_002_000000000pvtpDisplay.ScaleFactor = 0.09450006484985352
    ibm_fim_002_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_002_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GaussianRadius = 0.004725003242492676
    ibm_fim_002_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_002_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_001_000000000pvtp
    ibm_fim_001_000000000pvtpDisplay = Show(ibm_fim_001_000000000pvtp, renderView5, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_001_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_001_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_001_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_001_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_001_000000000pvtpDisplay.ScaleFactor = 1.8512276996023616
    ibm_fim_001_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_001_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GaussianRadius = 0.09256138498011808
    ibm_fim_001_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_001_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_003_000000000pvtp
    ibm_fim_003_000000000pvtpDisplay = Show(ibm_fim_003_000000000pvtp, renderView5, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_003_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_003_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_003_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_003_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_003_000000000pvtpDisplay.ScaleFactor = 0.4997869968414307
    ibm_fim_003_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_003_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GaussianRadius = 0.024989349842071535
    ibm_fim_003_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_003_000000000pvtpDisplay.WriteLog = ''

    # show data from threshold1
    threshold1Display = Show(threshold1, renderView5, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'temperature'
    temperatureTF2D = GetTransferFunction2D('temperature')

    # get color transfer function/color map for 'temperature'
    temperatureLUT = GetColorTransferFunction('temperature')
    temperatureLUT.TransferFunction2D = temperatureTF2D
    temperatureLUT.RGBPoints = [901.9279399817863, 0.231373, 0.298039, 0.752941, 908.6549809527049, 0.865003, 0.865003, 0.865003, 915.3820219236237, 0.705882, 0.0156863, 0.14902]
    temperatureLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'temperature'
    temperaturePWF = GetOpacityTransferFunction('temperature')
    temperaturePWF.Points = [901.9279399817863, 0.0, 0.5, 0.0, 915.3820219236237, 1.0, 0.5, 0.0]
    temperaturePWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'temperature']
    threshold1Display.LookupTable = temperatureLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'Mach'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'None'
    threshold1Display.ScaleFactor = 1.8412500000000014
    threshold1Display.SelectScaleArray = 'Mach'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'Mach'
    threshold1Display.GaussianRadius = 0.09206250000000006
    threshold1Display.SetScaleArray = ['POINTS', 'Mach']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'Mach']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.ScalarOpacityFunction = temperaturePWF
    threshold1Display.ScalarOpacityUnitDistance = 0.6166319841883904
    threshold1Display.OpacityArrayName = ['POINTS', 'Mach']
    threshold1Display.SelectInputVectors = [None, '']
    threshold1Display.WriteLog = ''
    threshold1Display.RescaleTransferFunctionToDataRange(False, True)

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [0.0018666807468164744, 0.0, 0.5, 0.0, 0.24960872123230704, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [0.0018666807468164744, 0.0, 0.5, 0.0, 0.24960872123230704, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for temperatureLUT in view renderView1
    temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView5)
    temperatureLUTColorBar.Orientation = 'Horizontal'
    temperatureLUTColorBar.WindowLocation = 'Any Location'
    temperatureLUTColorBar.Position = [0.32, 0.12]
    temperatureLUTColorBar.Title = 'Temperatura [K]'
    temperatureLUTColorBar.ComponentTitle = ''
    temperatureLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    temperatureLUTColorBar.TitleFontSize = 20
    temperatureLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    temperatureLUTColorBar.LabelFontSize = 18
    temperatureLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    temperatureLUTColorBar.Visibility = 1

    # show color legend
    threshold1Display.SetScalarBarVisibility(renderView5, True)

    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------

    # create extractor
    pNG5 = CreateExtractor('PNG', renderView5, registrationName='PNG5')
    # trace defaults for the extractor.
    pNG5.Trigger = 'TimeValue'

    # init the 'PNG' selected for 'Writer'
    pNG5.Writer.FileName = 'temperature_'+file_id+'.png'
    pNG5.Writer.ImageResolution = [1254, 643]
    pNG5.Writer.TransparentBackground = 1
    pNG5.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG5)

############################################################################################
#         VORTMAG
############################################################################################

    # Create a new 'Render View'
    renderView6 = CreateView('RenderView')
    renderView6.ViewSize = [1254, 643]
    renderView6.AxesGrid = 'GridAxes3DActor'
    renderView6.OrientationAxesVisibility = 0
    renderView6.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView6.UseToneMapping = 1
    renderView6.Exposure = 2.2
    renderView6.StereoType = 'Crystal Eyes'
    renderView6.CameraPosition = [13.387304411089747, 6.0, 27.436631001770568]
    renderView6.CameraFocalPoint = [13.647033466856255, 6.0, -24.399737720075517]
    renderView6.CameraFocalDisk = 1.0
    renderView6.CameraParallelScale = 13.41640786499874
    renderView6.BackEnd = 'OSPRay raycaster'
    renderView6.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView6)
    layout1.SetSize(1254, 643)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView6)
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

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

    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=slice1)
    threshold1.Scalars = ['POINTS', 'ib_marker']
    threshold1.LowerThreshold = 1.0
    threshold1.UpperThreshold = 1.0
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView6'
    # ----------------------------------------------------------------

    # show data from ibm_fim_002_000000000pvtp
    ibm_fim_002_000000000pvtpDisplay = Show(ibm_fim_002_000000000pvtp, renderView6, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_002_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_002_000000000pvtpDisplay.AmbientColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_002_000000000pvtpDisplay.DiffuseColor = [0.7098039215686275, 0.7098039215686275, 0.7098039215686275]
    ibm_fim_002_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_002_000000000pvtpDisplay.ScaleFactor = 0.09450006484985352
    ibm_fim_002_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_002_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_002_000000000pvtpDisplay.GaussianRadius = 0.004725003242492676
    ibm_fim_002_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_002_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_002_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_002_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_002_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_001_000000000pvtp
    ibm_fim_001_000000000pvtpDisplay = Show(ibm_fim_001_000000000pvtp, renderView6, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_001_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_001_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_001_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_001_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_001_000000000pvtpDisplay.ScaleFactor = 1.8512276996023616
    ibm_fim_001_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_001_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_001_000000000pvtpDisplay.GaussianRadius = 0.09256138498011808
    ibm_fim_001_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_001_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_001_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_001_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_001_000000000pvtpDisplay.WriteLog = ''

    # show data from ibm_fim_003_000000000pvtp
    ibm_fim_003_000000000pvtpDisplay = Show(ibm_fim_003_000000000pvtp, renderView6, 'GeometryRepresentation')

    # trace defaults for the display properties.
    ibm_fim_003_000000000pvtpDisplay.Representation = 'Surface'
    ibm_fim_003_000000000pvtpDisplay.ColorArrayName = [None, '']
    ibm_fim_003_000000000pvtpDisplay.Opacity = 0.2
    ibm_fim_003_000000000pvtpDisplay.SelectTCoordArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectNormalArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.SelectTangentArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.SelectOrientationVectors = 'None'
    ibm_fim_003_000000000pvtpDisplay.ScaleFactor = 0.4997869968414307
    ibm_fim_003_000000000pvtpDisplay.SelectScaleArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GlyphType = 'Arrow'
    ibm_fim_003_000000000pvtpDisplay.GlyphTableIndexArray = 'None'
    ibm_fim_003_000000000pvtpDisplay.GaussianRadius = 0.024989349842071535
    ibm_fim_003_000000000pvtpDisplay.SetScaleArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.OpacityArray = [None, '']
    ibm_fim_003_000000000pvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    ibm_fim_003_000000000pvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.PolarAxes = 'PolarAxesRepresentation'
    ibm_fim_003_000000000pvtpDisplay.SelectInputVectors = [None, '']
    ibm_fim_003_000000000pvtpDisplay.WriteLog = ''

    # show data from threshold1
    threshold1Display = Show(threshold1, renderView6, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'vortmag'
    vortmagTF2D = GetTransferFunction2D('vortmag')

    # get color transfer function/color map for 'vortmag'
    vortmagLUT = GetColorTransferFunction('vortmag')
    vortmagLUT.TransferFunction2D = vortmagTF2D
    vortmagLUT.RGBPoints = [-10.692328500783224, 0.231373, 0.298039, 0.752941, 2369.7633925657337, 0.865003, 0.865003, 0.865003, 4750.219113632251, 0.705882, 0.0156863, 0.14902]
    vortmagLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'vortmag'
    vortmagPWF = GetOpacityTransferFunction('vortmag')
    vortmagPWF.Points = [-10.692328500783224, 0.0, 0.5, 0.0, 4750.219113632251, 1.0, 0.5, 0.0]
    vortmagPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'vortmag']
    threshold1Display.LookupTable = vortmagLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'Mach'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'None'
    threshold1Display.ScaleFactor = 1.8412500000000014
    threshold1Display.SelectScaleArray = 'Mach'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'Mach'
    threshold1Display.GaussianRadius = 0.09206250000000006
    threshold1Display.SetScaleArray = ['POINTS', 'Mach']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'Mach']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.ScalarOpacityFunction = vortmagPWF
    threshold1Display.ScalarOpacityUnitDistance = 0.6166319841883904
    threshold1Display.OpacityArrayName = ['POINTS', 'Mach']
    threshold1Display.SelectInputVectors = [None, '']
    threshold1Display.WriteLog = ''
    threshold1Display.RescaleTransferFunctionToDataRange(False, True)

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [0.0018666807468164744, 0.0, 0.5, 0.0, 0.24960872123230704, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [0.0018666807468164744, 0.0, 0.5, 0.0, 0.24960872123230704, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for vortmagLUT in view renderView6
    vortmagLUTColorBar = GetScalarBar(vortmagLUT, renderView6)
    vortmagLUTColorBar.Orientation = 'Horizontal'
    vortmagLUTColorBar.WindowLocation = 'Any Location'
    vortmagLUTColorBar.Position = [0.32, 0.12]
    vortmagLUTColorBar.Title = 'Magnitude da vorticidade'
    vortmagLUTColorBar.ComponentTitle = ''
    vortmagLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    vortmagLUTColorBar.TitleFontSize = 20
    vortmagLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    vortmagLUTColorBar.LabelFontSize = 18
    vortmagLUTColorBar.ScalarBarLength = 0.32999999999999996
    vortmagLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    vortmagLUTColorBar.Visibility = 1

    # show color legend
    threshold1Display.SetScalarBarVisibility(renderView6, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------

    # create extractor
    pNG6 = CreateExtractor('PNG', renderView6, registrationName='PNG6')
    # trace defaults for the extractor.
    pNG6.Trigger = 'TimeValue'

    # init the 'PNG' selected for 'Writer'
    pNG6.Writer.FileName = 'vortmag_'+file_id+'.png'
    pNG6.Writer.ImageResolution = [1254, 643]
    pNG6.Writer.TransparentBackground = 1
    pNG6.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG6)


    # Create a new 'Render View'
    renderView7 = CreateView('RenderView')
    renderView7.ViewSize = [1254, 643]
    renderView7.AxesGrid = 'GridAxes3DActor'
    renderView7.OrientationAxesVisibility = 0
    renderView7.CenterOfRotation = [13.5, 6.0, 4.944999933242798]
    renderView7.StereoType = 'Crystal Eyes'
    renderView7.CameraPosition = [13.5, 6.0, 27.436913333807976]
    renderView7.CameraFocalPoint = [13.5, 6.0, -24.400106077512277]
    renderView7.CameraFocalDisk = 1.0
    renderView7.CameraParallelScale = 13.41640786499874
    renderView7.BackEnd = 'OSPRay raycaster'
    renderView7.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView7)
    layout1.SetSize(1254, 643)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView7)
    # ----------------------------------------------------------------

    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=calculator1)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.Triangulatetheslice = 0
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [13.500000000000005, 6.000000000000005, 4.945]
    slice1.SliceType.Normal = [0.0, 0.0, 1.0]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [13.500000000000005, 6.000000000000005, 5.099999999999999]

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView7'
    # ----------------------------------------------------------------

    # show data from slice1
    slice1Display = Show(slice1, renderView7, 'GeometryRepresentation')

    # get 2D transfer function for 'velocity'
    velocityTF2D = GetTransferFunction2D('velocity')

    # get color transfer function/color map for 'velocity'
    velocityLUT = GetColorTransferFunction('velocity')
    velocityLUT.TransferFunction2D = velocityTF2D
    velocityLUT.RGBPoints = [0.015658476057405522, 0.231373, 0.298039, 0.752941, 167.89742211881122, 0.865003, 0.865003, 0.865003, 335.77918576156503, 0.705882, 0.0156863, 0.14902]
    velocityLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = ['POINTS', 'velocity']
    slice1Display.LookupTable = velocityLUT
    slice1Display.SelectTCoordArray = 'None'
    slice1Display.SelectNormalArray = 'None'
    slice1Display.SelectTangentArray = 'None'
    slice1Display.OSPRayScaleArray = 'Mach'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'velocity'
    slice1Display.ScaleFactor = 2.4000000000000012
    slice1Display.SelectScaleArray = 'Mach'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'Mach'
    slice1Display.GaussianRadius = 0.12000000000000005
    slice1Display.SetScaleArray = ['POINTS', 'Mach']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'Mach']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.SelectInputVectors = ['POINTS', 'velocity']
    slice1Display.WriteLog = ''
    slice1Display.RescaleTransferFunctionToDataRange(False, True)


    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [-0.0007564060353854335, 0.0, 0.5, 0.0, 0.13228073098689977, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [-0.0007564060353854335, 0.0, 0.5, 0.0, 0.13228073098689977, 1.0, 0.5, 0.0]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for velocityLUT in view renderView7
    velocityLUTColorBar = GetScalarBar(velocityLUT, renderView7)
    velocityLUTColorBar.Orientation = 'Horizontal'
    velocityLUTColorBar.WindowLocation = 'Any Location'
    velocityLUTColorBar.Position = [0.32, 0.12]
    velocityLUTColorBar.Title = 'Magnitude da velocidade [m/s]'
    velocityLUTColorBar.ComponentTitle = 'Magnitude'
    velocityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    velocityLUTColorBar.TitleFontSize = 20
    velocityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    velocityLUTColorBar.LabelFontSize = 18
    velocityLUTColorBar.ScalarBarLength = 0.33000000000000035
    velocityLUTColorBar.RangeLabelFormat = '%-#6.1f'

    # set color bar visibility
    velocityLUTColorBar.Visibility = 1

    # show color legend
    slice1Display.SetScalarBarVisibility(renderView7, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get opacity transfer function/opacity map for 'velocity'
    velocityPWF = GetOpacityTransferFunction('velocity')
    velocityPWF.Points = [0.015658476057405522, 0.0, 0.5, 0.0, 335.77918576156503, 1.0, 0.5, 0.0]
    velocityPWF.ScalarRangeInitialized = 1

    # create extractor
    pNG7 = CreateExtractor('PNG', renderView7, registrationName='PNG7')
    # trace defaults for the extractor.
    pNG7.Trigger = 'TimeValue'

    # init the 'PNG' selected for 'Writer'
    pNG7.Writer.FileName = 'velmag_'+file_id+'.png'
    pNG7.Writer.ImageResolution = [1254, 643]
    pNG7.Writer.TransparentBackground = 1
    pNG7.Writer.Format = 'PNG'

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG7)

    # Catalyst options
    from paraview import catalyst

    directory = 'paraview_'+file_id+'_ct'+ct
    # path = os.path.join(output_path,directory)
    path = result_path
    os.makedirs(path,exist_ok = True)
    options = catalyst.Options()
    options.ExtractsOutputDirectory = path
    options.GlobalTrigger = 'TimeValue'
    options.CatalystLiveTrigger = 'TimeStep'

    print('PARAVIEW OUTPUT PATH: ', path)
    # init the 'TimeValue' selected for 'GlobalTrigger'
    # options.GlobalTrigger.Length = 1.0
    SaveExtractsUsingCatalystOptions(options)

