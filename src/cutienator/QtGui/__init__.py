"""
The 'cutienator.QtGui' package provides the cute classes of the part of
Qt named QtGui, under the name PySide6 has for it.

  from cutienator.QtGui import BMP_FILEHDR, BMP_INFOHDR

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'BMP_FILEHDR',
    'BMP_INFOHDR',
    'DataPtrContainer',
    'DrawHelper',
    'FontFile',
    'IntermediateBuffer',
    'LinearGradientValues',
    'Operator',
    'QAbstractUndoItem',
    'QAccessibleHyperlinkInterface',
    'QAccessibleImageInterface',
    'QAccessibleTableCellInterface',
    'QBrushData',
    'QColorTransferFunction',
    'QColorTransferGenericFunction',
    'QConicalGradientData',
    'QDBusMenuEvent',
    'QDBusMenuItemKeys',
    'QDBusTrayImage',
    'QDitherInfo',
    'QEdidVendorId',
    'QFixed',
    'QFontDef',
    'QFontEngineData',
    'QGles2SamplerData',
    'QGles2SamplerDescription',
    'QGles2UniformDescription',
    'QGles2UniformState',
    'QGlyphAttributes',
    'QGlyphJustification',
    'QGlyphLayout',
    'QGradientData',
    'QGridLayoutBox',
    'QGridLayoutMultiCellData',
    'QGridLayoutRowInfo',
    'QKeyBinding',
    'QLinearGradientData',
    'QOpenGLContextVersionFunctionHelper',
    'QPaintEngineState',
    'QPainterDummyState',
    'QPainterPathStrokerPrivate',
    'QPathEdge',
    'QPicturePrivate',
    'QPixelLayout',
    'QPlatformDropQtResponse',
    'QPlatformScreenPrivate',
    'QPlatformThemePrivate',
    'QPlatformWindowPrivate',
    'QPolylineSet',
    'QRadialGradientData',
    'QRealRect',
    'QRgba64',
    'QRhiAdapter',
    'QRhiBufferDataPrivate',
    'QRhiDepthStencilClearValue',
    'QRhiDriverInfo',
    'QRhiGlobalObjectIdGenerator',
    'QRhiIndexedIndirectDrawCommand',
    'QRhiIndirectDrawCommand',
    'QRhiInitParams',
    'QRhiNativeHandles',
    'QRhiReadbackResult',
    'QRhiRenderTargetAttachmentTracker',
    'QRhiScissor',
    'QRhiStats',
    'QRhiSwapChainHdrInfo',
    'QRhiSwapChainProxyData',
    'QRhiVertexInputAttribute',
    'QRhiVertexInputBinding',
    'QRhiViewport',
    'QScreenData',
    'QScriptAnalysis',
    'QShaderVersion',
    'QSpiAccessibleCacheItem',
    'QSpiAction',
    'QSpiDeviceEvent',
    'QSpiEventListener',
    'QSpiMatchRule',
    'QSpiTextRange',
    'QStaticTextUserData',
    'QStretchParameter',
    'QT_FT_BBox_',
    'QT_FT_Bitmap_',
    'QT_FT_Outline_',
    'QT_FT_Outline_Funcs_',
    'QT_FT_Raster_Funcs_',
    'QT_FT_Raster_Params_',
    'QT_FT_Span_',
    'QT_FT_Vector_',
    'QTextBlockData',
    'QTextBlockUserData',
    'QTextFragmentData',
    'QTextFrameLayoutData',
    'QTextHtmlElement',
    'QTextItem',
    'QTextLength',
    'QTextObjectHandler',
    'QTextOption',
    'QTextUndoCommand',
    'QTextureData',
    'QThemeIconInfo',
    'QTransformImageVertex',
    'QTriangleSet',
    'QUndoCommandPrivate',
    'QVertexIndexVector',
    'QVkRenderTargetData',
    'QVulkanDefaultInstance',
    'QVulkanExtension',
    'QVulkanLayer',
    'QVulkanWindowRenderer',
    'QXdgDBusImageStruct',
    'QXdgDBusToolTipStruct',
    'QtFontFallbacksCacheKey',
    'QtFontSize',
    'QtFontStyle',
    'RadialGradientValues',
    'qfixed2d',
    'quint24',
    'QBrushDataPointerDeleter',
    'QColorTransferTable',
    'QGenericUnixThemePrivate',
    'QGridLayoutRowData',
    'QPageRangesPrivate',
    'QRhiGles2NativeHandles',
    'QRhiMetalCommandBufferNativeHandles',
    'QRhiMetalInitParams',
    'QRhiMetalNativeHandles',
    'QRhiNullInitParams',
    'QRhiNullNativeHandles',
    'QRhiVertexInputLayout',
    'QRhiVulkanCommandBufferNativeHandles',
    'QRhiVulkanInitParams',
    'QRhiVulkanNativeHandles',
    'QRhiVulkanQueueSubmitParams',
    'QRhiVulkanRenderPassNativeHandles',
    'QScriptItem',
    'QVarLengthGlyphLayoutArray',
    'QVectorPathConverter',
    'QVulkanAdapter',
    'QWindowSystemEventHandler',
    'QAccessibleViewportInterface',
    'QColorTrc',
    'QColorVector',
    'QEdidParser',
    'QFixedPoint',
    'QOpenGLExtensionMatcher',
    'QOpenGLProgramBinaryCache',
    'QPathVertex',
    'QRhiBufferData',
    'QRhiPipelineCacheDataReader',
    'QRhiTextureCopyDescription',
    'QShaderCode',
    'QX11Info',
    'QAccessibleActionInterface',
    'QAccessibleEditableTextInterface',
    'QColor',
    'QColorCLUT',
    'QColorMatrix',
    'QColorTrcLut',
    'QFixedSize',
    'QGenericPluginFactory',
    'QGnomeThemePrivate',
    'QIconDirInfo',
    'QIconLoader',
    'QIconTheme',
    'QPageRanges',
    'QPageSize',
    'QPdfPage',
    'QPlatformDragQtResponse',
    'QPlatformInputContextFactory',
    'QPlatformIntegrationFactory',
    'QPlatformThemeFactory',
    'QPolygon',
    'QUndoCommand',
    'QtFontFamily',
    'QCmyk32',
    'QColorTransform',
    'QGridLayoutItem',
    'QPageLayout',
    'QPolygonF',
    'QtFontFoundry',
    'QAccessibilityHints',
    'QAccessibleBridgePlugin',
    'QAccessiblePlugin',
    'QAccessibleValueInterface',
    'QApplicationStateChangeEvent',
    'QCloseEvent',
    'QColorDialogOptions',
    'QColorSpace',
    'QColorTransformPrivate',
    'QDesktopServices',
    'QDragLeaveEvent',
    'QDragPrivate',
    'QDropEvent',
    'QFocusEvent',
    'QFontDialogOptions',
    'QFontVariableAxis',
    'QGenericPlugin',
    'QGradient',
    'QHelpEvent',
    'QHideEvent',
    'QIconDragEvent',
    'QIconEnginePlugin',
    'QImageIOPlugin',
    'QInputDevice',
    'QInputDevicePrivate',
    'QInputDeviceManager',
    'QInputMethodEvent',
    'QInputMethodQueryEvent',
    'QInternalMimeData',
    'QKeySequence',
    'QLayoutPolicy',
    'QMoveEvent',
    'QOpenGLConfig',
    'QOpenGLContextGroup',
    'QPixelFormat',
    'QPlatformBackingStoreRhiConfig',
    'QPlatformInputContextPlugin',
    'QPlatformInputContextPrivate',
    'QPlatformIntegrationPlugin',
    'QPlatformServiceColorPicker',
    'QPlatformSurfaceEvent',
    'QPlatformThemePlugin',
    'QPointingDeviceUniqueId',
    'QResizeEvent',
    'QScreenPrivate',
    'QScrollEvent',
    'QScrollPrepareEvent',
    'QSessionManagerPrivate',
    'QShaderDescription',
    'QShowEvent',
    'QStandardItemData',
    'QStatusTipEvent',
    'QStyleHints',
    'QSurface',
    'QTextureFileHandler',
    'QTextureFileReader',
    'QToolBarChangeEvent',
    'QUndoStack',
    'QUtiMimeConverter',
    'QValidator',
    'QWhatsThisClickedEvent',
    'QWindowStateChangeEvent',
    'QWindowsMimeConverter',
    'QAbstractLayoutStyleInfo',
    'QAccessibilityHintsPrivate',
    'QAstcHandler',
    'QTransform',
    'QFont',
    'QRegion',
    'QFontInfo',
    'QFontDatabase',
    'QImageIOHandler',
    'QImageReader',
    'QPaintDevice',
    'QImage',
    'QBrush',
    'QImageWriter',
    'QPainterPath',
    'QPen',
    'QRawFont',
    'QGlyphRun',
    'QStaticText',
    'QFontPrivate',
    'QPicture',
    'QPixmap',
    'QBitmap',
    'QPainter',
    'QPlatformPixmap',
    'QColorSpacePrivate',
    'QConicalGradient',
    'QDBusListener',
    'QDBusMenuRegistrarInterface',
    'QDoubleValidator',
    'QDragMoveEvent',
    'QInputDeviceManagerPrivate',
    'QInputEvent',
    'QIntValidator',
    'QKeySequencePrivate',
    'QKtxHandler',
    'QLinearGradient',
    'QPAEventDispatcherGlibPrivate',
    'QPdfOutputIntent',
    'QPkmHandler',
    'QPlatformGraphicsBuffer',
    'QPlatformSurface',
    'QRadialGradient',
    'QRegularExpressionValidator',
    'QShader',
    'QShaderKey',
    'QShaderDescriptionPrivate',
    'QShortcut',
    'QSpiObjectReference',
    'QSurfaceFormat',
    'QUndoGroup',
    'QXdgNotificationInterface',
    'QBezier',
    'QBmpHandler',
    'QClipData',
    'QClipboard',
    'QColrPaintGraphRenderer',
    'QContextMenuEvent',
    'QCursorData',
    'QDistanceFieldData',
    'QDrag',
    'QDragEnterEvent',
    'QExposeEvent',
    'QFileOpenEvent',
    'QFontDatabasePrivate',
    'QFontMetrics',
    'QGlyphRunPrivate',
    'QGnomePortalInterface',
    'QGridLayoutEngine',
    'QImageData',
    'QImagePixmapCleanupHooks',
    'QInputMethod',
    'QKeyEvent',
    'QVector4D',
    'QVector3D',
    'QQuaternion',
    'QMatrix4x4',
    'QVector2D',
    'QMovie',
    'QPAEventDispatcherGlib',
    'QPagedPaintDevice',
    'QPagedPaintDevicePrivate',
    'QPaintEvent',
    'QPainterClipInfo',
    'QPainterPathPrivate',
    'QPainterPathStroker',
    'QPainterState',
    'QPainterStateGuard',
    'QPalette',
    'QPathSegments',
    'QPenPrivate',
    'QPixmapCache',
    'QPixmapCacheEntry',
    'QPlatformCursorImage',
    'QPlatformSharedGraphicsCache',
    'QPngHandler',
    'QPpmHandler',
    'QRasterBuffer',
    'QRasterPlatformPixmap',
    'QRasterizer',
    'QRhiGles2InitParams',
    'QRhiShaderStage',
    'QRhiTextureSubresourceUploadDescription',
    'QShaderPrivate',
    'QShortcutEvent',
    'QSpiDBusCache',
    'QStaticTextPrivate',
    'QStrokerOps',
    'QSupportedWritingSystems',
    'QTextFormat',
    'QTextureFileData',
    'QUnixEventDispatcherQPA',
    'QWingedEdge',
    'QXbmHandler',
    'QXpmHandler',
    'glyph_metrics_t',
    'QDragManager',
    'QEventPoint',
    'QPointerEvent',
    'QPointingDevice',
    'QTouchEvent',
    'QPointingDevicePrivate',
    'QFileDialogOptions',
    'QFontEngine',
    'QFontEngineGlyphCache',
    'QFontMetricsF',
    'QInputControl',
    'QInputMethodPrivate',
    'QKeyMapper',
    'QPalettePrivate',
    'QPathClipper',
    'QPdfWriter',
    'QPlatformClipboard',
    'QPlatformDrag',
    'QPlatformInputContext',
    'QPlatformKeyMapper',
    'QRasterPaintEngineState',
    'QRhiTextureUploadEntry',
    'QShortcutMap',
    'QSpiApplicationAdaptor',
    'QStroker',
    'QTextBlockFormat',
    'QTextCharFormat',
    'QTextFormatCollection',
    'QTextFrameFormat',
    'QTextListFormat',
    'QBlittable',
    'QDashStroker',
    'QDistanceField',
    'QEventPointPrivate',
    'QFontCache',
    'QFontEngineMulti',
    'QFontSubset',
    'QMutableTouchEvent',
    'QPlatformFontDatabase',
    'QRawFontPrivate',
    'QRhiTextureUploadDescription',
    'QShortcutPrivate',
    'QSinglePointEvent',
    'QStaticTextItem',
    'QTextImageFormat',
    'QTextItemInt',
    'QTextTableCellFormat',
    'QTextTableFormat',
    'QTextureGlyphCache',
    'QAbstractFileIconProvider',
    'QAbstractFileIconProviderPrivate',
    'QTextDocument',
    'QTextBlock',
    'QTextEngine',
    'QTextInlineObject',
    'QTextLayout',
    'QTextObjectPrivate',
    'QTextFramePrivate',
    'QTextObject',
    'QTextFrame',
    'QAbstractTextDocumentLayout',
    'QTextDocumentPrivate',
    'QTextCursor',
    'QTextTable',
    'QAbstractTextDocumentLayoutPrivate',
    'QScriptLine',
    'QTextCursorPrivate',
    'QTextDocumentFragment',
    'QEnterEvent',
    'QExtendedInformation',
    'QFileSystemModelPrivate',
    'QFreeTypeFontDatabase',
    'QHoverEvent',
    'QImageTextureGlyphCache',
    'QMouseEvent',
    'QMutableSinglePointEvent',
    'QNativeGestureEvent',
    'QPaintEngine',
    'QPaintEnginePrivate',
    'QPlatformTheme',
    'QTabletEvent',
    'QWheelEvent',
    'QAccessibleInterface',
    'QAccessible',
    'QAccessibleEvent',
    'QScreen',
    'QCursor',
    'QWindow',
    'QIcon',
    'QIconEngine',
    'QPlatformScreen',
    'QVulkanInstance',
    'QWindowPrivate',
    'QFileInfoGatherer',
    'QFileSystemModel',
    'QFontEngineBox',
    'QFontconfigDatabase',
    'QGenericUnixTheme',
    'QPaintEngineExPrivate',
    'QPainterPrivate',
    'QPdfEnginePrivate',
    'QPicturePaintEngine',
    'QStackTextEngine',
    'QStyleHintsPrivate',
    'QSyntaxHighlighter',
    'QTextBlockGroupPrivate',
    'QTextCopyHelper',
    'QTextDocumentFragmentPrivate',
    'QTextDocumentWriter',
    'QTextFragment',
    'QTextHtmlParser',
    'QTextLine',
    'QTextLineItemIterator',
    'QTextMarkdownImporter',
    'QTextObjectInterface',
    'QTextTableCell',
    'QTextTablePrivate',
    'QAccessibleAnnouncementEvent',
    'QAccessibleAttributesInterface',
    'QAccessibleBridge',
    'QAccessibleCache',
    'QAccessibleObject',
    'QAccessibleObjectDestroyedEvent',
    'QAccessibleSelectionInterface',
    'QAccessibleStateChangeEvent',
    'QAccessibleTableModelChangeEvent',
    'QAccessibleTextCursorEvent',
    'QAccessibleTextInterface',
    'QAccessibleValueChangeEvent',
    'QAction',
    'QActionGroupPrivate',
    'QActionGroup',
    'QActionPrivate',
    'QBackingStore',
    'QBackingStoreRhiSupport',
    'QBasicDrag',
    'QChildWindowEvent',
    'QFontIconEngine',
    'QGnomeTheme',
    'QHighDpiScaling',
    'QIconLoaderEngine',
    'QIconLoaderEngineEntry',
    'QIconPrivate',
    'QKdeTheme',
    'QMutableEventPoint',
    'QOffscreenSurface',
    'QOpenGLContext',
    'QPaintDeviceWindowPrivate',
    'QPaintEngineEx',
    'QVectorPath',
    'QPdfEngine',
    'QPixmapIconEngineEntry',
    'QPlatformAccessibility',
    'QPlatformCursor',
    'QPlatformDialogHelper',
    'QPlatformMenu',
    'QPlatformMenuItem',
    'QPlatformPlaceholderScreen',
    'QPlatformServices',
    'QPlatformVulkanInstance',
    'QPlatformWindow',
    'QProxyIconEngine',
    'QRhiReadbackDescription',
    'QRhiResource',
    'QRhiTexture',
    'QRhiBuffer',
    'QRhiRenderBuffer',
    'QRhiRenderPassDescriptor',
    'QRhiSampler',
    'QRhiShaderResourceBinding',
    'QRhiShaderResourceBindings',
    'QRhiColorAttachment',
    'QRhiTextureRenderTargetDescription',
    'QRhiComputePipeline',
    'QRhiGraphicsPipeline',
    'QRhiRenderTarget',
    'QRhiResourceUpdateBatch',
    'QRhiCommandBuffer',
    'QRhiTextureRenderTarget',
    'QRhi',
    'QRhiImplementation',
    'QRhiShadingRateMap',
    'QRhiSwapChain',
    'QScreenOrientationChangeEvent',
    'QStandardItem',
    'QStandardItemModelPrivate',
    'QStandardItemModel',
    'QStandardItemPrivate',
    'QTestFontEngine',
    'QTextBlockGroup',
    'QTextDocumentLayout',
    'QTextHtmlExporter',
    'QTextHtmlImporter',
    'QTextHtmlParserNode',
    'QTextImageHandler',
    'QTextOdfWriter',
    'QVulkanWindow',
    'QVulkanWindowPrivate',
    'QWindowSystemInterface',
    'QWindowSystemInterfacePrivate',
    'PixmapEntry',
    'QAccessibleApplication',
    'QAccessibleTableInterface',
    'QAccessibleTextInsertEvent',
    'QAccessibleTextRemoveEvent',
    'QAccessibleTextSelectionEvent',
    'QAccessibleTextUpdateEvent',
    'QActionEvent',
    'QBackingStoreRhiSupportWindowWatcher',
    'QBasicPlatformVulkanInstance',
    'QBlittablePlatformPixmap',
    'QCosmeticStroker',
    'QDBusPlatformMenuItem',
    'QDashedStrokeProcessor',
    'QDesktopUnixServices',
    'QEmulationPaintEngine',
    'QGles2Buffer',
    'QGles2CommandBuffer',
    'QGles2ComputePipeline',
    'QGles2GraphicsPipeline',
    'QGles2RenderBuffer',
    'QGles2RenderPassDescriptor',
    'QGles2RenderTargetData',
    'QGles2Sampler',
    'QGles2ShaderResourceBindings',
    'QGles2Texture',
    'QGles2TextureRenderTarget',
    'QGraphicsFrameCapture',
    'QGraphicsFrameCapturePrivate',
    'QMessageDialogOptions',
    'QMetalBuffer',
    'QMetalCommandBuffer',
    'QMetalComputePipeline',
    'QMetalRenderBuffer',
    'QMetalRenderPassDescriptor',
    'QMetalSampler',
    'QMetalShaderResourceBindings',
    'QMetalShadingRateMap',
    'QMetalSwapChain',
    'QMetalTexture',
    'QMetalTextureRenderTarget',
    'QNullBuffer',
    'QNullCommandBuffer',
    'QNullComputePipeline',
    'QNullGraphicsPipeline',
    'QNullRenderBuffer',
    'QNullRenderPassDescriptor',
    'QNullRenderTargetData',
    'QNullSampler',
    'QNullShaderResourceBindings',
    'QNullSwapChain',
    'QNullTexture',
    'QNullTextureRenderTarget',
    'QOffscreenSurfacePrivate',
    'QOpenGLContextGroupPrivate',
    'QOpenGLFunctionsPrivate',
    'QOpenGLProgramBinarySupportCheckWrapper',
    'QOpenGLSharedResource',
    'QOutlineMapper',
    'QPaintDeviceWindow',
    'QPixmapIconEngine',
    'QPlatformColorDialogHelper',
    'QPlatformFileDialogHelper',
    'QPlatformFontDialogHelper',
    'QPlatformIntegration',
    'QPlatformMenuBar',
    'QPlatformNativeInterface',
    'QPlatformOffscreenSurface',
    'QPlatformOpenGLContext',
    'QPlatformSystemTrayIcon',
    'QPlatformTextureList',
    'QSpanData',
    'QRasterPaintEnginePrivate',
    'QRasterPaintEngine',
    'QRhiPassResourceTracker',
    'QRhiResourceUpdateBatchPrivate',
    'QRhiSwapChainRenderTarget',
    'QSimpleDrag',
    'QSpiAccessibleBridge',
    'QTextList',
    'QThemeIconEngine',
    'QTriangulatingStroker',
    'QUndoStackPrivate',
    'QVkBuffer',
    'QVkCommandBuffer',
    'QVkComputePipeline',
    'QVkGraphicsPipeline',
    'QVkRenderBuffer',
    'QVkRenderPassDescriptor',
    'QVkSampler',
    'QVkShaderResourceBindings',
    'QVkShadingRateMap',
    'QVkSwapChain',
    'QVkTexture',
    'QVkTextureRenderTarget',
    'ScalableEntry',
    'QAbstractFileIconEngine',
    'QBlitterPaintEngine',
    'QDBusMenuBar',
    'QDBusMenuItem',
    'QDBusPlatformMenu',
    'QDBusTrayIcon',
    'QGles2SwapChainRenderTarget',
    'QGraphicsFrameCaptureMetal',
    'QMetalGraphicsPipeline',
    'QMetalSwapChainRenderTarget',
    'QNullSwapChainRenderTarget',
    'QOpenGLContextPrivate',
    'QOpenGLExtraFunctionsPrivate',
    'QOpenGLFunctions',
    'QOpenGLMultiGroupSharedResource',
    'QOpenGLProgramBinarySupportCheck',
    'QOpenGLSharedResourceGuard',
    'QPlatformBackingStore',
    'QPlatformMessageDialogHelper',
    'QRasterWindow',
    'QRhiGles2',
    'QRhiMetal',
    'QRhiNull',
    'QRhiVulkan',
    'QTextMarkdownWriter',
    'QVkSwapChainRenderTarget',
    'QBackingStoreDefaultCompositor',
    'QDBusMenuConnection',
    'QDBusMenuLayoutItem',
    'QGles2SwapChain',
    'QGles2SwapChainTimestamps',
    'QOpenGLExtensionsPrivate',
    'QOpenGLExtraFunctions',
    'QRasterBackingStore',
    'QShapedPixmapWindow',
    'QStatusNotifierItemAdaptor',
    'QDBusMenuAdaptor',
    'QOpenGLExtensions',
    'QRhiBackingStore',
    'QGuiApplicationPrivate',
    'QGuiApplication',
    'QSessionManager',
    'QPlatformSessionManager',
    'QDBusMenuEventList',
    'QDBusMenuItemKeysList',
    'QSpiAccessibleCacheArray',
    'QXdgDBusImageVector',
    'QWindowList',
    'QDBusMenuItemList',
    'QCss',
    'QGuiSvg',
    'QImageReaderWriterHelpers',
    'QImageScale',
    'QNativeInterface',
    'QPdf',
    'QTest',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._b_m_p_f_i_l_e_h_d_r import BMP_FILEHDR
  from ._b_m_p_i_n_f_o_h_d_r import BMP_INFOHDR
  from ._data_ptr_container import DataPtrContainer
  from ._draw_helper import DrawHelper
  from ._font_file import FontFile
  from ._intermediate_buffer import IntermediateBuffer
  from ._linear_gradient_values import LinearGradientValues
  from ._operator import Operator
  from ._q_abstract_undo_item import QAbstractUndoItem
  from ._q_accessible_hyperlink_interface import QAccessibleHyperlinkInterface
  from ._q_accessible_image_interface import QAccessibleImageInterface
  from ._q_accessible_table_cell_interface import QAccessibleTableCellInterface
  from ._q_brush_data import QBrushData
  from ._q_color_transfer_function import QColorTransferFunction
  from ._q_color_transfer_generic_function import QColorTransferGenericFunction
  from ._q_conical_gradient_data import QConicalGradientData
  from ._q_d_bus_menu_event import QDBusMenuEvent
  from ._q_d_bus_menu_item_keys import QDBusMenuItemKeys
  from ._q_d_bus_tray_image import QDBusTrayImage
  from ._q_dither_info import QDitherInfo
  from ._q_edid_vendor_id import QEdidVendorId
  from ._q_fixed import QFixed
  from ._q_font_def import QFontDef
  from ._q_font_engine_data import QFontEngineData
  from ._q_gles2_sampler_data import QGles2SamplerData
  from ._q_gles2_sampler_description import QGles2SamplerDescription
  from ._q_gles2_uniform_description import QGles2UniformDescription
  from ._q_gles2_uniform_state import QGles2UniformState
  from ._q_glyph_attributes import QGlyphAttributes
  from ._q_glyph_justification import QGlyphJustification
  from ._q_glyph_layout import QGlyphLayout
  from ._q_gradient_data import QGradientData
  from ._q_grid_layout_box import QGridLayoutBox
  from ._q_grid_layout_multi_cell_data import QGridLayoutMultiCellData
  from ._q_grid_layout_row_info import QGridLayoutRowInfo
  from ._q_key_binding import QKeyBinding
  from ._q_linear_gradient_data import QLinearGradientData
  from ._q_open_g_l_context_version_function_helper import QOpenGLContextVersionFunctionHelper
  from ._q_paint_engine_state import QPaintEngineState
  from ._q_painter_dummy_state import QPainterDummyState
  from ._q_painter_path_stroker_private import QPainterPathStrokerPrivate
  from ._q_path_edge import QPathEdge
  from ._q_picture_private import QPicturePrivate
  from ._q_pixel_layout import QPixelLayout
  from ._q_platform_drop_qt_response import QPlatformDropQtResponse
  from ._q_platform_screen_private import QPlatformScreenPrivate
  from ._q_platform_theme_private import QPlatformThemePrivate
  from ._q_platform_window_private import QPlatformWindowPrivate
  from ._q_polyline_set import QPolylineSet
  from ._q_radial_gradient_data import QRadialGradientData
  from ._q_real_rect import QRealRect
  from ._q_rgba64 import QRgba64
  from ._q_rhi_adapter import QRhiAdapter
  from ._q_rhi_buffer_data_private import QRhiBufferDataPrivate
  from ._q_rhi_depth_stencil_clear_value import QRhiDepthStencilClearValue
  from ._q_rhi_driver_info import QRhiDriverInfo
  from ._q_rhi_global_object_id_generator import QRhiGlobalObjectIdGenerator
  from ._q_rhi_indexed_indirect_draw_command import QRhiIndexedIndirectDrawCommand
  from ._q_rhi_indirect_draw_command import QRhiIndirectDrawCommand
  from ._q_rhi_init_params import QRhiInitParams
  from ._q_rhi_native_handles import QRhiNativeHandles
  from ._q_rhi_readback_result import QRhiReadbackResult
  from ._q_rhi_render_target_attachment_tracker import QRhiRenderTargetAttachmentTracker
  from ._q_rhi_scissor import QRhiScissor
  from ._q_rhi_stats import QRhiStats
  from ._q_rhi_swap_chain_hdr_info import QRhiSwapChainHdrInfo
  from ._q_rhi_swap_chain_proxy_data import QRhiSwapChainProxyData
  from ._q_rhi_vertex_input_attribute import QRhiVertexInputAttribute
  from ._q_rhi_vertex_input_binding import QRhiVertexInputBinding
  from ._q_rhi_viewport import QRhiViewport
  from ._q_screen_data import QScreenData
  from ._q_script_analysis import QScriptAnalysis
  from ._q_shader_version import QShaderVersion
  from ._q_spi_accessible_cache_item import QSpiAccessibleCacheItem
  from ._q_spi_action import QSpiAction
  from ._q_spi_device_event import QSpiDeviceEvent
  from ._q_spi_event_listener import QSpiEventListener
  from ._q_spi_match_rule import QSpiMatchRule
  from ._q_spi_text_range import QSpiTextRange
  from ._q_static_text_user_data import QStaticTextUserData
  from ._q_stretch_parameter import QStretchParameter
  from ._q_t_f_t_b_box_ import QT_FT_BBox_
  from ._q_t_f_t_bitmap_ import QT_FT_Bitmap_
  from ._q_t_f_t_outline_ import QT_FT_Outline_
  from ._q_t_f_t_outline_funcs_ import QT_FT_Outline_Funcs_
  from ._q_t_f_t_raster_funcs_ import QT_FT_Raster_Funcs_
  from ._q_t_f_t_raster_params_ import QT_FT_Raster_Params_
  from ._q_t_f_t_span_ import QT_FT_Span_
  from ._q_t_f_t_vector_ import QT_FT_Vector_
  from ._q_text_block_data import QTextBlockData
  from ._q_text_block_user_data import QTextBlockUserData
  from ._q_text_fragment_data import QTextFragmentData
  from ._q_text_frame_layout_data import QTextFrameLayoutData
  from ._q_text_html_element import QTextHtmlElement
  from ._q_text_item import QTextItem
  from ._q_text_length import QTextLength
  from ._q_text_object_handler import QTextObjectHandler
  from ._q_text_option import QTextOption
  from ._q_text_undo_command import QTextUndoCommand
  from ._q_texture_data import QTextureData
  from ._q_theme_icon_info import QThemeIconInfo
  from ._q_transform_image_vertex import QTransformImageVertex
  from ._q_triangle_set import QTriangleSet
  from ._q_undo_command_private import QUndoCommandPrivate
  from ._q_vertex_index_vector import QVertexIndexVector
  from ._q_vk_render_target_data import QVkRenderTargetData
  from ._q_vulkan_default_instance import QVulkanDefaultInstance
  from ._q_vulkan_extension import QVulkanExtension
  from ._q_vulkan_layer import QVulkanLayer
  from ._q_vulkan_window_renderer import QVulkanWindowRenderer
  from ._q_xdg_d_bus_image_struct import QXdgDBusImageStruct
  from ._q_xdg_d_bus_tool_tip_struct import QXdgDBusToolTipStruct
  from ._qt_font_fallbacks_cache_key import QtFontFallbacksCacheKey
  from ._qt_font_size import QtFontSize
  from ._qt_font_style import QtFontStyle
  from ._radial_gradient_values import RadialGradientValues
  from ._qfixed2d import qfixed2d
  from ._quint24 import quint24
  from ._q_brush_data_pointer_deleter import QBrushDataPointerDeleter
  from ._q_color_transfer_table import QColorTransferTable
  from ._q_generic_unix_theme_private import QGenericUnixThemePrivate
  from ._q_grid_layout_row_data import QGridLayoutRowData
  from ._q_page_ranges_private import QPageRangesPrivate
  from ._q_rhi_gles2_native_handles import QRhiGles2NativeHandles
  from ._q_rhi_metal_command_buffer_native_handles import QRhiMetalCommandBufferNativeHandles
  from ._q_rhi_metal_init_params import QRhiMetalInitParams
  from ._q_rhi_metal_native_handles import QRhiMetalNativeHandles
  from ._q_rhi_null_init_params import QRhiNullInitParams
  from ._q_rhi_null_native_handles import QRhiNullNativeHandles
  from ._q_rhi_vertex_input_layout import QRhiVertexInputLayout
  from ._q_rhi_vulkan_command_buffer_native_handles import QRhiVulkanCommandBufferNativeHandles
  from ._q_rhi_vulkan_init_params import QRhiVulkanInitParams
  from ._q_rhi_vulkan_native_handles import QRhiVulkanNativeHandles
  from ._q_rhi_vulkan_queue_submit_params import QRhiVulkanQueueSubmitParams
  from ._q_rhi_vulkan_render_pass_native_handles import QRhiVulkanRenderPassNativeHandles
  from ._q_script_item import QScriptItem
  from ._q_var_length_glyph_layout_array import QVarLengthGlyphLayoutArray
  from ._q_vector_path_converter import QVectorPathConverter
  from ._q_vulkan_adapter import QVulkanAdapter
  from ._q_window_system_event_handler import QWindowSystemEventHandler
  from ._q_accessible_viewport_interface import QAccessibleViewportInterface
  from ._q_color_trc import QColorTrc
  from ._q_color_vector import QColorVector
  from ._q_edid_parser import QEdidParser
  from ._q_fixed_point import QFixedPoint
  from ._q_open_g_l_extension_matcher import QOpenGLExtensionMatcher
  from ._q_open_g_l_program_binary_cache import QOpenGLProgramBinaryCache
  from ._q_path_vertex import QPathVertex
  from ._q_rhi_buffer_data import QRhiBufferData
  from ._q_rhi_pipeline_cache_data_reader import QRhiPipelineCacheDataReader
  from ._q_rhi_texture_copy_description import QRhiTextureCopyDescription
  from ._q_shader_code import QShaderCode
  from ._q_x11_info import QX11Info
  from ._q_accessible_action_interface import QAccessibleActionInterface
  from ._q_accessible_editable_text_interface import QAccessibleEditableTextInterface
  from ._q_color import QColor
  from ._q_color_c_l_u_t import QColorCLUT
  from ._q_color_matrix import QColorMatrix
  from ._q_color_trc_lut import QColorTrcLut
  from ._q_fixed_size import QFixedSize
  from ._q_generic_plugin_factory import QGenericPluginFactory
  from ._q_gnome_theme_private import QGnomeThemePrivate
  from ._q_icon_dir_info import QIconDirInfo
  from ._q_icon_loader import QIconLoader
  from ._q_icon_theme import QIconTheme
  from ._q_page_ranges import QPageRanges
  from ._q_page_size import QPageSize
  from ._q_pdf_page import QPdfPage
  from ._q_platform_drag_qt_response import QPlatformDragQtResponse
  from ._q_platform_input_context_factory import QPlatformInputContextFactory
  from ._q_platform_integration_factory import QPlatformIntegrationFactory
  from ._q_platform_theme_factory import QPlatformThemeFactory
  from ._q_polygon import QPolygon
  from ._q_undo_command import QUndoCommand
  from ._qt_font_family import QtFontFamily
  from ._q_cmyk32 import QCmyk32
  from ._q_color_transform import QColorTransform
  from ._q_grid_layout_item import QGridLayoutItem
  from ._q_page_layout import QPageLayout
  from ._q_polygon_f import QPolygonF
  from ._qt_font_foundry import QtFontFoundry
  from ._q_accessibility_hints import QAccessibilityHints
  from ._q_accessible_bridge_plugin import QAccessibleBridgePlugin
  from ._q_accessible_plugin import QAccessiblePlugin
  from ._q_accessible_value_interface import QAccessibleValueInterface
  from ._q_application_state_change_event import QApplicationStateChangeEvent
  from ._q_close_event import QCloseEvent
  from ._q_color_dialog_options import QColorDialogOptions
  from ._q_color_space import QColorSpace
  from ._q_color_transform_private import QColorTransformPrivate
  from ._q_desktop_services import QDesktopServices
  from ._q_drag_leave_event import QDragLeaveEvent
  from ._q_drag_private import QDragPrivate
  from ._q_drop_event import QDropEvent
  from ._q_focus_event import QFocusEvent
  from ._q_font_dialog_options import QFontDialogOptions
  from ._q_font_variable_axis import QFontVariableAxis
  from ._q_generic_plugin import QGenericPlugin
  from ._q_gradient import QGradient
  from ._q_help_event import QHelpEvent
  from ._q_hide_event import QHideEvent
  from ._q_icon_drag_event import QIconDragEvent
  from ._q_icon_engine_plugin import QIconEnginePlugin
  from ._q_image_i_o_plugin import QImageIOPlugin
  from ._q_input_device import QInputDevice
  from ._q_input_device_private import QInputDevicePrivate
  from ._q_input_device_manager import QInputDeviceManager
  from ._q_input_method_event import QInputMethodEvent
  from ._q_input_method_query_event import QInputMethodQueryEvent
  from ._q_internal_mime_data import QInternalMimeData
  from ._q_key_sequence import QKeySequence
  from ._q_layout_policy import QLayoutPolicy
  from ._q_move_event import QMoveEvent
  from ._q_open_g_l_config import QOpenGLConfig
  from ._q_open_g_l_context_group import QOpenGLContextGroup
  from ._q_pixel_format import QPixelFormat
  from ._q_platform_backing_store_rhi_config import QPlatformBackingStoreRhiConfig
  from ._q_platform_input_context_plugin import QPlatformInputContextPlugin
  from ._q_platform_input_context_private import QPlatformInputContextPrivate
  from ._q_platform_integration_plugin import QPlatformIntegrationPlugin
  from ._q_platform_service_color_picker import QPlatformServiceColorPicker
  from ._q_platform_surface_event import QPlatformSurfaceEvent
  from ._q_platform_theme_plugin import QPlatformThemePlugin
  from ._q_pointing_device_unique_id import QPointingDeviceUniqueId
  from ._q_resize_event import QResizeEvent
  from ._q_screen_private import QScreenPrivate
  from ._q_scroll_event import QScrollEvent
  from ._q_scroll_prepare_event import QScrollPrepareEvent
  from ._q_session_manager_private import QSessionManagerPrivate
  from ._q_shader_description import QShaderDescription
  from ._q_show_event import QShowEvent
  from ._q_standard_item_data import QStandardItemData
  from ._q_status_tip_event import QStatusTipEvent
  from ._q_style_hints import QStyleHints
  from ._q_surface import QSurface
  from ._q_texture_file_handler import QTextureFileHandler
  from ._q_texture_file_reader import QTextureFileReader
  from ._q_tool_bar_change_event import QToolBarChangeEvent
  from ._q_undo_stack import QUndoStack
  from ._q_uti_mime_converter import QUtiMimeConverter
  from ._q_validator import QValidator
  from ._q_whats_this_clicked_event import QWhatsThisClickedEvent
  from ._q_window_state_change_event import QWindowStateChangeEvent
  from ._q_windows_mime_converter import QWindowsMimeConverter
  from ._q_abstract_layout_style_info import QAbstractLayoutStyleInfo
  from ._q_accessibility_hints_private import QAccessibilityHintsPrivate
  from ._q_astc_handler import QAstcHandler
  from ._q_transform import QTransform
  from ._q_font import QFont
  from ._q_region import QRegion
  from ._q_font_info import QFontInfo
  from ._q_font_database import QFontDatabase
  from ._q_image_i_o_handler import QImageIOHandler
  from ._q_image_reader import QImageReader
  from ._q_paint_device import QPaintDevice
  from ._q_image import QImage
  from ._q_brush import QBrush
  from ._q_image_writer import QImageWriter
  from ._q_painter_path import QPainterPath
  from ._q_pen import QPen
  from ._q_raw_font import QRawFont
  from ._q_glyph_run import QGlyphRun
  from ._q_static_text import QStaticText
  from ._q_font_private import QFontPrivate
  from ._q_picture import QPicture
  from ._q_pixmap import QPixmap
  from ._q_bitmap import QBitmap
  from ._q_painter import QPainter
  from ._q_platform_pixmap import QPlatformPixmap
  from ._q_color_space_private import QColorSpacePrivate
  from ._q_conical_gradient import QConicalGradient
  from ._q_d_bus_listener import QDBusListener
  from ._q_d_bus_menu_registrar_interface import QDBusMenuRegistrarInterface
  from ._q_double_validator import QDoubleValidator
  from ._q_drag_move_event import QDragMoveEvent
  from ._q_input_device_manager_private import QInputDeviceManagerPrivate
  from ._q_input_event import QInputEvent
  from ._q_int_validator import QIntValidator
  from ._q_key_sequence_private import QKeySequencePrivate
  from ._q_ktx_handler import QKtxHandler
  from ._q_linear_gradient import QLinearGradient
  from ._q_p_a_event_dispatcher_glib_private import QPAEventDispatcherGlibPrivate
  from ._q_pdf_output_intent import QPdfOutputIntent
  from ._q_pkm_handler import QPkmHandler
  from ._q_platform_graphics_buffer import QPlatformGraphicsBuffer
  from ._q_platform_surface import QPlatformSurface
  from ._q_radial_gradient import QRadialGradient
  from ._q_regular_expression_validator import QRegularExpressionValidator
  from ._q_shader import QShader
  from ._q_shader_key import QShaderKey
  from ._q_shader_description_private import QShaderDescriptionPrivate
  from ._q_shortcut import QShortcut
  from ._q_spi_object_reference import QSpiObjectReference
  from ._q_surface_format import QSurfaceFormat
  from ._q_undo_group import QUndoGroup
  from ._q_xdg_notification_interface import QXdgNotificationInterface
  from ._q_bezier import QBezier
  from ._q_bmp_handler import QBmpHandler
  from ._q_clip_data import QClipData
  from ._q_clipboard import QClipboard
  from ._q_colr_paint_graph_renderer import QColrPaintGraphRenderer
  from ._q_context_menu_event import QContextMenuEvent
  from ._q_cursor_data import QCursorData
  from ._q_distance_field_data import QDistanceFieldData
  from ._q_drag import QDrag
  from ._q_drag_enter_event import QDragEnterEvent
  from ._q_expose_event import QExposeEvent
  from ._q_file_open_event import QFileOpenEvent
  from ._q_font_database_private import QFontDatabasePrivate
  from ._q_font_metrics import QFontMetrics
  from ._q_glyph_run_private import QGlyphRunPrivate
  from ._q_gnome_portal_interface import QGnomePortalInterface
  from ._q_grid_layout_engine import QGridLayoutEngine
  from ._q_image_data import QImageData
  from ._q_image_pixmap_cleanup_hooks import QImagePixmapCleanupHooks
  from ._q_input_method import QInputMethod
  from ._q_key_event import QKeyEvent
  from ._q_vector4_d import QVector4D
  from ._q_vector3_d import QVector3D
  from ._q_quaternion import QQuaternion
  from ._q_matrix4x4 import QMatrix4x4
  from ._q_vector2_d import QVector2D
  from ._q_movie import QMovie
  from ._q_p_a_event_dispatcher_glib import QPAEventDispatcherGlib
  from ._q_paged_paint_device import QPagedPaintDevice
  from ._q_paged_paint_device_private import QPagedPaintDevicePrivate
  from ._q_paint_event import QPaintEvent
  from ._q_painter_clip_info import QPainterClipInfo
  from ._q_painter_path_private import QPainterPathPrivate
  from ._q_painter_path_stroker import QPainterPathStroker
  from ._q_painter_state import QPainterState
  from ._q_painter_state_guard import QPainterStateGuard
  from ._q_palette import QPalette
  from ._q_path_segments import QPathSegments
  from ._q_pen_private import QPenPrivate
  from ._q_pixmap_cache import QPixmapCache
  from ._q_pixmap_cache_entry import QPixmapCacheEntry
  from ._q_platform_cursor_image import QPlatformCursorImage
  from ._q_platform_shared_graphics_cache import QPlatformSharedGraphicsCache
  from ._q_png_handler import QPngHandler
  from ._q_ppm_handler import QPpmHandler
  from ._q_raster_buffer import QRasterBuffer
  from ._q_raster_platform_pixmap import QRasterPlatformPixmap
  from ._q_rasterizer import QRasterizer
  from ._q_rhi_gles2_init_params import QRhiGles2InitParams
  from ._q_rhi_shader_stage import QRhiShaderStage
  from ._q_rhi_texture_subresource_upload_description import QRhiTextureSubresourceUploadDescription
  from ._q_shader_private import QShaderPrivate
  from ._q_shortcut_event import QShortcutEvent
  from ._q_spi_d_bus_cache import QSpiDBusCache
  from ._q_static_text_private import QStaticTextPrivate
  from ._q_stroker_ops import QStrokerOps
  from ._q_supported_writing_systems import QSupportedWritingSystems
  from ._q_text_format import QTextFormat
  from ._q_texture_file_data import QTextureFileData
  from ._q_unix_event_dispatcher_q_p_a import QUnixEventDispatcherQPA
  from ._q_winged_edge import QWingedEdge
  from ._q_xbm_handler import QXbmHandler
  from ._q_xpm_handler import QXpmHandler
  from ._glyph_metrics_t import glyph_metrics_t
  from ._q_drag_manager import QDragManager
  from ._q_event_point import QEventPoint
  from ._q_pointer_event import QPointerEvent
  from ._q_pointing_device import QPointingDevice
  from ._q_touch_event import QTouchEvent
  from ._q_pointing_device_private import QPointingDevicePrivate
  from ._q_file_dialog_options import QFileDialogOptions
  from ._q_font_engine import QFontEngine
  from ._q_font_engine_glyph_cache import QFontEngineGlyphCache
  from ._q_font_metrics_f import QFontMetricsF
  from ._q_input_control import QInputControl
  from ._q_input_method_private import QInputMethodPrivate
  from ._q_key_mapper import QKeyMapper
  from ._q_palette_private import QPalettePrivate
  from ._q_path_clipper import QPathClipper
  from ._q_pdf_writer import QPdfWriter
  from ._q_platform_clipboard import QPlatformClipboard
  from ._q_platform_drag import QPlatformDrag
  from ._q_platform_input_context import QPlatformInputContext
  from ._q_platform_key_mapper import QPlatformKeyMapper
  from ._q_raster_paint_engine_state import QRasterPaintEngineState
  from ._q_rhi_texture_upload_entry import QRhiTextureUploadEntry
  from ._q_shortcut_map import QShortcutMap
  from ._q_spi_application_adaptor import QSpiApplicationAdaptor
  from ._q_stroker import QStroker
  from ._q_text_block_format import QTextBlockFormat
  from ._q_text_char_format import QTextCharFormat
  from ._q_text_format_collection import QTextFormatCollection
  from ._q_text_frame_format import QTextFrameFormat
  from ._q_text_list_format import QTextListFormat
  from ._q_blittable import QBlittable
  from ._q_dash_stroker import QDashStroker
  from ._q_distance_field import QDistanceField
  from ._q_event_point_private import QEventPointPrivate
  from ._q_font_cache import QFontCache
  from ._q_font_engine_multi import QFontEngineMulti
  from ._q_font_subset import QFontSubset
  from ._q_mutable_touch_event import QMutableTouchEvent
  from ._q_platform_font_database import QPlatformFontDatabase
  from ._q_raw_font_private import QRawFontPrivate
  from ._q_rhi_texture_upload_description import QRhiTextureUploadDescription
  from ._q_shortcut_private import QShortcutPrivate
  from ._q_single_point_event import QSinglePointEvent
  from ._q_static_text_item import QStaticTextItem
  from ._q_text_image_format import QTextImageFormat
  from ._q_text_item_int import QTextItemInt
  from ._q_text_table_cell_format import QTextTableCellFormat
  from ._q_text_table_format import QTextTableFormat
  from ._q_texture_glyph_cache import QTextureGlyphCache
  from ._q_abstract_file_icon_provider import QAbstractFileIconProvider
  from ._q_abstract_file_icon_provider_private import QAbstractFileIconProviderPrivate
  from ._q_text_document import QTextDocument
  from ._q_text_block import QTextBlock
  from ._q_text_engine import QTextEngine
  from ._q_text_inline_object import QTextInlineObject
  from ._q_text_layout import QTextLayout
  from ._q_text_object_private import QTextObjectPrivate
  from ._q_text_frame_private import QTextFramePrivate
  from ._q_text_object import QTextObject
  from ._q_text_frame import QTextFrame
  from ._q_abstract_text_document_layout import QAbstractTextDocumentLayout
  from ._q_text_document_private import QTextDocumentPrivate
  from ._q_text_cursor import QTextCursor
  from ._q_text_table import QTextTable
  from ._q_abstract_text_document_layout_private import QAbstractTextDocumentLayoutPrivate
  from ._q_script_line import QScriptLine
  from ._q_text_cursor_private import QTextCursorPrivate
  from ._q_text_document_fragment import QTextDocumentFragment
  from ._q_enter_event import QEnterEvent
  from ._q_extended_information import QExtendedInformation
  from ._q_file_system_model_private import QFileSystemModelPrivate
  from ._q_free_type_font_database import QFreeTypeFontDatabase
  from ._q_hover_event import QHoverEvent
  from ._q_image_texture_glyph_cache import QImageTextureGlyphCache
  from ._q_mouse_event import QMouseEvent
  from ._q_mutable_single_point_event import QMutableSinglePointEvent
  from ._q_native_gesture_event import QNativeGestureEvent
  from ._q_paint_engine import QPaintEngine
  from ._q_paint_engine_private import QPaintEnginePrivate
  from ._q_platform_theme import QPlatformTheme
  from ._q_tablet_event import QTabletEvent
  from ._q_wheel_event import QWheelEvent
  from ._q_accessible_interface import QAccessibleInterface
  from ._q_accessible import QAccessible
  from ._q_accessible_event import QAccessibleEvent
  from ._q_screen import QScreen
  from ._q_cursor import QCursor
  from ._q_window import QWindow
  from ._q_icon import QIcon
  from ._q_icon_engine import QIconEngine
  from ._q_platform_screen import QPlatformScreen
  from ._q_vulkan_instance import QVulkanInstance
  from ._q_window_private import QWindowPrivate
  from ._q_file_info_gatherer import QFileInfoGatherer
  from ._q_file_system_model import QFileSystemModel
  from ._q_font_engine_box import QFontEngineBox
  from ._q_fontconfig_database import QFontconfigDatabase
  from ._q_generic_unix_theme import QGenericUnixTheme
  from ._q_paint_engine_ex_private import QPaintEngineExPrivate
  from ._q_painter_private import QPainterPrivate
  from ._q_pdf_engine_private import QPdfEnginePrivate
  from ._q_picture_paint_engine import QPicturePaintEngine
  from ._q_stack_text_engine import QStackTextEngine
  from ._q_style_hints_private import QStyleHintsPrivate
  from ._q_syntax_highlighter import QSyntaxHighlighter
  from ._q_text_block_group_private import QTextBlockGroupPrivate
  from ._q_text_copy_helper import QTextCopyHelper
  from ._q_text_document_fragment_private import QTextDocumentFragmentPrivate
  from ._q_text_document_writer import QTextDocumentWriter
  from ._q_text_fragment import QTextFragment
  from ._q_text_html_parser import QTextHtmlParser
  from ._q_text_line import QTextLine
  from ._q_text_line_item_iterator import QTextLineItemIterator
  from ._q_text_markdown_importer import QTextMarkdownImporter
  from ._q_text_object_interface import QTextObjectInterface
  from ._q_text_table_cell import QTextTableCell
  from ._q_text_table_private import QTextTablePrivate
  from ._q_accessible_announcement_event import QAccessibleAnnouncementEvent
  from ._q_accessible_attributes_interface import QAccessibleAttributesInterface
  from ._q_accessible_bridge import QAccessibleBridge
  from ._q_accessible_cache import QAccessibleCache
  from ._q_accessible_object import QAccessibleObject
  from ._q_accessible_object_destroyed_event import QAccessibleObjectDestroyedEvent
  from ._q_accessible_selection_interface import QAccessibleSelectionInterface
  from ._q_accessible_state_change_event import QAccessibleStateChangeEvent
  from ._q_accessible_table_model_change_event import QAccessibleTableModelChangeEvent
  from ._q_accessible_text_cursor_event import QAccessibleTextCursorEvent
  from ._q_accessible_text_interface import QAccessibleTextInterface
  from ._q_accessible_value_change_event import QAccessibleValueChangeEvent
  from ._q_action import QAction
  from ._q_action_group_private import QActionGroupPrivate
  from ._q_action_group import QActionGroup
  from ._q_action_private import QActionPrivate
  from ._q_backing_store import QBackingStore
  from ._q_backing_store_rhi_support import QBackingStoreRhiSupport
  from ._q_basic_drag import QBasicDrag
  from ._q_child_window_event import QChildWindowEvent
  from ._q_font_icon_engine import QFontIconEngine
  from ._q_gnome_theme import QGnomeTheme
  from ._q_high_dpi_scaling import QHighDpiScaling
  from ._q_icon_loader_engine import QIconLoaderEngine
  from ._q_icon_loader_engine_entry import QIconLoaderEngineEntry
  from ._q_icon_private import QIconPrivate
  from ._q_kde_theme import QKdeTheme
  from ._q_mutable_event_point import QMutableEventPoint
  from ._q_offscreen_surface import QOffscreenSurface
  from ._q_open_g_l_context import QOpenGLContext
  from ._q_paint_device_window_private import QPaintDeviceWindowPrivate
  from ._q_paint_engine_ex import QPaintEngineEx
  from ._q_vector_path import QVectorPath
  from ._q_pdf_engine import QPdfEngine
  from ._q_pixmap_icon_engine_entry import QPixmapIconEngineEntry
  from ._q_platform_accessibility import QPlatformAccessibility
  from ._q_platform_cursor import QPlatformCursor
  from ._q_platform_dialog_helper import QPlatformDialogHelper
  from ._q_platform_menu import QPlatformMenu
  from ._q_platform_menu_item import QPlatformMenuItem
  from ._q_platform_placeholder_screen import QPlatformPlaceholderScreen
  from ._q_platform_services import QPlatformServices
  from ._q_platform_vulkan_instance import QPlatformVulkanInstance
  from ._q_platform_window import QPlatformWindow
  from ._q_proxy_icon_engine import QProxyIconEngine
  from ._q_rhi_readback_description import QRhiReadbackDescription
  from ._q_rhi_resource import QRhiResource
  from ._q_rhi_texture import QRhiTexture
  from ._q_rhi_buffer import QRhiBuffer
  from ._q_rhi_render_buffer import QRhiRenderBuffer
  from ._q_rhi_render_pass_descriptor import QRhiRenderPassDescriptor
  from ._q_rhi_sampler import QRhiSampler
  from ._q_rhi_shader_resource_binding import QRhiShaderResourceBinding
  from ._q_rhi_shader_resource_bindings import QRhiShaderResourceBindings
  from ._q_rhi_color_attachment import QRhiColorAttachment
  from ._q_rhi_texture_render_target_description import QRhiTextureRenderTargetDescription
  from ._q_rhi_compute_pipeline import QRhiComputePipeline
  from ._q_rhi_graphics_pipeline import QRhiGraphicsPipeline
  from ._q_rhi_render_target import QRhiRenderTarget
  from ._q_rhi_resource_update_batch import QRhiResourceUpdateBatch
  from ._q_rhi_command_buffer import QRhiCommandBuffer
  from ._q_rhi_texture_render_target import QRhiTextureRenderTarget
  from ._q_rhi import QRhi
  from ._q_rhi_implementation import QRhiImplementation
  from ._q_rhi_shading_rate_map import QRhiShadingRateMap
  from ._q_rhi_swap_chain import QRhiSwapChain
  from ._q_screen_orientation_change_event import QScreenOrientationChangeEvent
  from ._q_standard_item import QStandardItem
  from ._q_standard_item_model_private import QStandardItemModelPrivate
  from ._q_standard_item_model import QStandardItemModel
  from ._q_standard_item_private import QStandardItemPrivate
  from ._q_test_font_engine import QTestFontEngine
  from ._q_text_block_group import QTextBlockGroup
  from ._q_text_document_layout import QTextDocumentLayout
  from ._q_text_html_exporter import QTextHtmlExporter
  from ._q_text_html_importer import QTextHtmlImporter
  from ._q_text_html_parser_node import QTextHtmlParserNode
  from ._q_text_image_handler import QTextImageHandler
  from ._q_text_odf_writer import QTextOdfWriter
  from ._q_vulkan_window import QVulkanWindow
  from ._q_vulkan_window_private import QVulkanWindowPrivate
  from ._q_window_system_interface import QWindowSystemInterface
  from ._q_window_system_interface_private import QWindowSystemInterfacePrivate
  from ._pixmap_entry import PixmapEntry
  from ._q_accessible_application import QAccessibleApplication
  from ._q_accessible_table_interface import QAccessibleTableInterface
  from ._q_accessible_text_insert_event import QAccessibleTextInsertEvent
  from ._q_accessible_text_remove_event import QAccessibleTextRemoveEvent
  from ._q_accessible_text_selection_event import QAccessibleTextSelectionEvent
  from ._q_accessible_text_update_event import QAccessibleTextUpdateEvent
  from ._q_action_event import QActionEvent
  from ._q_backing_store_rhi_support_window_watcher import QBackingStoreRhiSupportWindowWatcher
  from ._q_basic_platform_vulkan_instance import QBasicPlatformVulkanInstance
  from ._q_blittable_platform_pixmap import QBlittablePlatformPixmap
  from ._q_cosmetic_stroker import QCosmeticStroker
  from ._q_d_bus_platform_menu_item import QDBusPlatformMenuItem
  from ._q_dashed_stroke_processor import QDashedStrokeProcessor
  from ._q_desktop_unix_services import QDesktopUnixServices
  from ._q_emulation_paint_engine import QEmulationPaintEngine
  from ._q_gles2_buffer import QGles2Buffer
  from ._q_gles2_command_buffer import QGles2CommandBuffer
  from ._q_gles2_compute_pipeline import QGles2ComputePipeline
  from ._q_gles2_graphics_pipeline import QGles2GraphicsPipeline
  from ._q_gles2_render_buffer import QGles2RenderBuffer
  from ._q_gles2_render_pass_descriptor import QGles2RenderPassDescriptor
  from ._q_gles2_render_target_data import QGles2RenderTargetData
  from ._q_gles2_sampler import QGles2Sampler
  from ._q_gles2_shader_resource_bindings import QGles2ShaderResourceBindings
  from ._q_gles2_texture import QGles2Texture
  from ._q_gles2_texture_render_target import QGles2TextureRenderTarget
  from ._q_graphics_frame_capture import QGraphicsFrameCapture
  from ._q_graphics_frame_capture_private import QGraphicsFrameCapturePrivate
  from ._q_message_dialog_options import QMessageDialogOptions
  from ._q_metal_buffer import QMetalBuffer
  from ._q_metal_command_buffer import QMetalCommandBuffer
  from ._q_metal_compute_pipeline import QMetalComputePipeline
  from ._q_metal_render_buffer import QMetalRenderBuffer
  from ._q_metal_render_pass_descriptor import QMetalRenderPassDescriptor
  from ._q_metal_sampler import QMetalSampler
  from ._q_metal_shader_resource_bindings import QMetalShaderResourceBindings
  from ._q_metal_shading_rate_map import QMetalShadingRateMap
  from ._q_metal_swap_chain import QMetalSwapChain
  from ._q_metal_texture import QMetalTexture
  from ._q_metal_texture_render_target import QMetalTextureRenderTarget
  from ._q_null_buffer import QNullBuffer
  from ._q_null_command_buffer import QNullCommandBuffer
  from ._q_null_compute_pipeline import QNullComputePipeline
  from ._q_null_graphics_pipeline import QNullGraphicsPipeline
  from ._q_null_render_buffer import QNullRenderBuffer
  from ._q_null_render_pass_descriptor import QNullRenderPassDescriptor
  from ._q_null_render_target_data import QNullRenderTargetData
  from ._q_null_sampler import QNullSampler
  from ._q_null_shader_resource_bindings import QNullShaderResourceBindings
  from ._q_null_swap_chain import QNullSwapChain
  from ._q_null_texture import QNullTexture
  from ._q_null_texture_render_target import QNullTextureRenderTarget
  from ._q_offscreen_surface_private import QOffscreenSurfacePrivate
  from ._q_open_g_l_context_group_private import QOpenGLContextGroupPrivate
  from ._q_open_g_l_functions_private import QOpenGLFunctionsPrivate
  from ._q_open_g_l_program_binary_support_check_wrapper import QOpenGLProgramBinarySupportCheckWrapper
  from ._q_open_g_l_shared_resource import QOpenGLSharedResource
  from ._q_outline_mapper import QOutlineMapper
  from ._q_paint_device_window import QPaintDeviceWindow
  from ._q_pixmap_icon_engine import QPixmapIconEngine
  from ._q_platform_color_dialog_helper import QPlatformColorDialogHelper
  from ._q_platform_file_dialog_helper import QPlatformFileDialogHelper
  from ._q_platform_font_dialog_helper import QPlatformFontDialogHelper
  from ._q_platform_integration import QPlatformIntegration
  from ._q_platform_menu_bar import QPlatformMenuBar
  from ._q_platform_native_interface import QPlatformNativeInterface
  from ._q_platform_offscreen_surface import QPlatformOffscreenSurface
  from ._q_platform_open_g_l_context import QPlatformOpenGLContext
  from ._q_platform_system_tray_icon import QPlatformSystemTrayIcon
  from ._q_platform_texture_list import QPlatformTextureList
  from ._q_span_data import QSpanData
  from ._q_raster_paint_engine_private import QRasterPaintEnginePrivate
  from ._q_raster_paint_engine import QRasterPaintEngine
  from ._q_rhi_pass_resource_tracker import QRhiPassResourceTracker
  from ._q_rhi_resource_update_batch_private import QRhiResourceUpdateBatchPrivate
  from ._q_rhi_swap_chain_render_target import QRhiSwapChainRenderTarget
  from ._q_simple_drag import QSimpleDrag
  from ._q_spi_accessible_bridge import QSpiAccessibleBridge
  from ._q_text_list import QTextList
  from ._q_theme_icon_engine import QThemeIconEngine
  from ._q_triangulating_stroker import QTriangulatingStroker
  from ._q_undo_stack_private import QUndoStackPrivate
  from ._q_vk_buffer import QVkBuffer
  from ._q_vk_command_buffer import QVkCommandBuffer
  from ._q_vk_compute_pipeline import QVkComputePipeline
  from ._q_vk_graphics_pipeline import QVkGraphicsPipeline
  from ._q_vk_render_buffer import QVkRenderBuffer
  from ._q_vk_render_pass_descriptor import QVkRenderPassDescriptor
  from ._q_vk_sampler import QVkSampler
  from ._q_vk_shader_resource_bindings import QVkShaderResourceBindings
  from ._q_vk_shading_rate_map import QVkShadingRateMap
  from ._q_vk_swap_chain import QVkSwapChain
  from ._q_vk_texture import QVkTexture
  from ._q_vk_texture_render_target import QVkTextureRenderTarget
  from ._scalable_entry import ScalableEntry
  from ._q_abstract_file_icon_engine import QAbstractFileIconEngine
  from ._q_blitter_paint_engine import QBlitterPaintEngine
  from ._q_d_bus_menu_bar import QDBusMenuBar
  from ._q_d_bus_menu_item import QDBusMenuItem
  from ._q_d_bus_platform_menu import QDBusPlatformMenu
  from ._q_d_bus_tray_icon import QDBusTrayIcon
  from ._q_gles2_swap_chain_render_target import QGles2SwapChainRenderTarget
  from ._q_graphics_frame_capture_metal import QGraphicsFrameCaptureMetal
  from ._q_metal_graphics_pipeline import QMetalGraphicsPipeline
  from ._q_metal_swap_chain_render_target import QMetalSwapChainRenderTarget
  from ._q_null_swap_chain_render_target import QNullSwapChainRenderTarget
  from ._q_open_g_l_context_private import QOpenGLContextPrivate
  from ._q_open_g_l_extra_functions_private import QOpenGLExtraFunctionsPrivate
  from ._q_open_g_l_functions import QOpenGLFunctions
  from ._q_open_g_l_multi_group_shared_resource import QOpenGLMultiGroupSharedResource
  from ._q_open_g_l_program_binary_support_check import QOpenGLProgramBinarySupportCheck
  from ._q_open_g_l_shared_resource_guard import QOpenGLSharedResourceGuard
  from ._q_platform_backing_store import QPlatformBackingStore
  from ._q_platform_message_dialog_helper import QPlatformMessageDialogHelper
  from ._q_raster_window import QRasterWindow
  from ._q_rhi_gles2 import QRhiGles2
  from ._q_rhi_metal import QRhiMetal
  from ._q_rhi_null import QRhiNull
  from ._q_rhi_vulkan import QRhiVulkan
  from ._q_text_markdown_writer import QTextMarkdownWriter
  from ._q_vk_swap_chain_render_target import QVkSwapChainRenderTarget
  from ._q_backing_store_default_compositor import QBackingStoreDefaultCompositor
  from ._q_d_bus_menu_connection import QDBusMenuConnection
  from ._q_d_bus_menu_layout_item import QDBusMenuLayoutItem
  from ._q_gles2_swap_chain import QGles2SwapChain
  from ._q_gles2_swap_chain_timestamps import QGles2SwapChainTimestamps
  from ._q_open_g_l_extensions_private import QOpenGLExtensionsPrivate
  from ._q_open_g_l_extra_functions import QOpenGLExtraFunctions
  from ._q_raster_backing_store import QRasterBackingStore
  from ._q_shaped_pixmap_window import QShapedPixmapWindow
  from ._q_status_notifier_item_adaptor import QStatusNotifierItemAdaptor
  from ._q_d_bus_menu_adaptor import QDBusMenuAdaptor
  from ._q_open_g_l_extensions import QOpenGLExtensions
  from ._q_rhi_backing_store import QRhiBackingStore
  from ._q_gui_application_private import QGuiApplicationPrivate
  from ._q_gui_application import QGuiApplication
  from ._q_session_manager import QSessionManager
  from ._q_platform_session_manager import QPlatformSessionManager
  from ._q_d_bus_menu_event import QDBusMenuEventList
  from ._q_d_bus_menu_item_keys import QDBusMenuItemKeysList
  from ._q_spi_accessible_cache_item import QSpiAccessibleCacheArray
  from ._q_xdg_d_bus_image_struct import QXdgDBusImageVector
  from ._q_window import QWindowList
  from ._q_d_bus_menu_item import QDBusMenuItemList
  from . import QCss
  from . import QGuiSvg
  from . import QImageReaderWriterHelpers
  from . import QImageScale
  from . import QNativeInterface
  from . import QPdf
  from . import QTest
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'BMP_FILEHDR': '_b_m_p_f_i_l_e_h_d_r',
      'BMP_INFOHDR': '_b_m_p_i_n_f_o_h_d_r',
      'DataPtrContainer': '_data_ptr_container',
      'DrawHelper': '_draw_helper',
      'FontFile': '_font_file',
      'IntermediateBuffer': '_intermediate_buffer',
      'LinearGradientValues': '_linear_gradient_values',
      'Operator': '_operator',
      'QAbstractUndoItem': '_q_abstract_undo_item',
      'QAccessibleHyperlinkInterface': '_q_accessible_hyperlink_interface',
      'QAccessibleImageInterface': '_q_accessible_image_interface',
      'QAccessibleTableCellInterface': '_q_accessible_table_cell_interface',
      'QBrushData': '_q_brush_data',
      'QColorTransferFunction': '_q_color_transfer_function',
      'QColorTransferGenericFunction': '_q_color_transfer_generic_function',
      'QConicalGradientData': '_q_conical_gradient_data',
      'QDBusMenuEvent': '_q_d_bus_menu_event',
      'QDBusMenuItemKeys': '_q_d_bus_menu_item_keys',
      'QDBusTrayImage': '_q_d_bus_tray_image',
      'QDitherInfo': '_q_dither_info',
      'QEdidVendorId': '_q_edid_vendor_id',
      'QFixed': '_q_fixed',
      'QFontDef': '_q_font_def',
      'QFontEngineData': '_q_font_engine_data',
      'QGles2SamplerData': '_q_gles2_sampler_data',
      'QGles2SamplerDescription': '_q_gles2_sampler_description',
      'QGles2UniformDescription': '_q_gles2_uniform_description',
      'QGles2UniformState': '_q_gles2_uniform_state',
      'QGlyphAttributes': '_q_glyph_attributes',
      'QGlyphJustification': '_q_glyph_justification',
      'QGlyphLayout': '_q_glyph_layout',
      'QGradientData': '_q_gradient_data',
      'QGridLayoutBox': '_q_grid_layout_box',
      'QGridLayoutMultiCellData': '_q_grid_layout_multi_cell_data',
      'QGridLayoutRowInfo': '_q_grid_layout_row_info',
      'QKeyBinding': '_q_key_binding',
      'QLinearGradientData': '_q_linear_gradient_data',
      'QOpenGLContextVersionFunctionHelper': '_q_open_g_l_context_version_function_helper',
      'QPaintEngineState': '_q_paint_engine_state',
      'QPainterDummyState': '_q_painter_dummy_state',
      'QPainterPathStrokerPrivate': '_q_painter_path_stroker_private',
      'QPathEdge': '_q_path_edge',
      'QPicturePrivate': '_q_picture_private',
      'QPixelLayout': '_q_pixel_layout',
      'QPlatformDropQtResponse': '_q_platform_drop_qt_response',
      'QPlatformScreenPrivate': '_q_platform_screen_private',
      'QPlatformThemePrivate': '_q_platform_theme_private',
      'QPlatformWindowPrivate': '_q_platform_window_private',
      'QPolylineSet': '_q_polyline_set',
      'QRadialGradientData': '_q_radial_gradient_data',
      'QRealRect': '_q_real_rect',
      'QRgba64': '_q_rgba64',
      'QRhiAdapter': '_q_rhi_adapter',
      'QRhiBufferDataPrivate': '_q_rhi_buffer_data_private',
      'QRhiDepthStencilClearValue': '_q_rhi_depth_stencil_clear_value',
      'QRhiDriverInfo': '_q_rhi_driver_info',
      'QRhiGlobalObjectIdGenerator': '_q_rhi_global_object_id_generator',
      'QRhiIndexedIndirectDrawCommand': '_q_rhi_indexed_indirect_draw_command',
      'QRhiIndirectDrawCommand': '_q_rhi_indirect_draw_command',
      'QRhiInitParams': '_q_rhi_init_params',
      'QRhiNativeHandles': '_q_rhi_native_handles',
      'QRhiReadbackResult': '_q_rhi_readback_result',
      'QRhiRenderTargetAttachmentTracker': '_q_rhi_render_target_attachment_tracker',
      'QRhiScissor': '_q_rhi_scissor',
      'QRhiStats': '_q_rhi_stats',
      'QRhiSwapChainHdrInfo': '_q_rhi_swap_chain_hdr_info',
      'QRhiSwapChainProxyData': '_q_rhi_swap_chain_proxy_data',
      'QRhiVertexInputAttribute': '_q_rhi_vertex_input_attribute',
      'QRhiVertexInputBinding': '_q_rhi_vertex_input_binding',
      'QRhiViewport': '_q_rhi_viewport',
      'QScreenData': '_q_screen_data',
      'QScriptAnalysis': '_q_script_analysis',
      'QShaderVersion': '_q_shader_version',
      'QSpiAccessibleCacheItem': '_q_spi_accessible_cache_item',
      'QSpiAction': '_q_spi_action',
      'QSpiDeviceEvent': '_q_spi_device_event',
      'QSpiEventListener': '_q_spi_event_listener',
      'QSpiMatchRule': '_q_spi_match_rule',
      'QSpiTextRange': '_q_spi_text_range',
      'QStaticTextUserData': '_q_static_text_user_data',
      'QStretchParameter': '_q_stretch_parameter',
      'QT_FT_BBox_': '_q_t_f_t_b_box_',
      'QT_FT_Bitmap_': '_q_t_f_t_bitmap_',
      'QT_FT_Outline_': '_q_t_f_t_outline_',
      'QT_FT_Outline_Funcs_': '_q_t_f_t_outline_funcs_',
      'QT_FT_Raster_Funcs_': '_q_t_f_t_raster_funcs_',
      'QT_FT_Raster_Params_': '_q_t_f_t_raster_params_',
      'QT_FT_Span_': '_q_t_f_t_span_',
      'QT_FT_Vector_': '_q_t_f_t_vector_',
      'QTextBlockData': '_q_text_block_data',
      'QTextBlockUserData': '_q_text_block_user_data',
      'QTextFragmentData': '_q_text_fragment_data',
      'QTextFrameLayoutData': '_q_text_frame_layout_data',
      'QTextHtmlElement': '_q_text_html_element',
      'QTextItem': '_q_text_item',
      'QTextLength': '_q_text_length',
      'QTextObjectHandler': '_q_text_object_handler',
      'QTextOption': '_q_text_option',
      'QTextUndoCommand': '_q_text_undo_command',
      'QTextureData': '_q_texture_data',
      'QThemeIconInfo': '_q_theme_icon_info',
      'QTransformImageVertex': '_q_transform_image_vertex',
      'QTriangleSet': '_q_triangle_set',
      'QUndoCommandPrivate': '_q_undo_command_private',
      'QVertexIndexVector': '_q_vertex_index_vector',
      'QVkRenderTargetData': '_q_vk_render_target_data',
      'QVulkanDefaultInstance': '_q_vulkan_default_instance',
      'QVulkanExtension': '_q_vulkan_extension',
      'QVulkanLayer': '_q_vulkan_layer',
      'QVulkanWindowRenderer': '_q_vulkan_window_renderer',
      'QXdgDBusImageStruct': '_q_xdg_d_bus_image_struct',
      'QXdgDBusToolTipStruct': '_q_xdg_d_bus_tool_tip_struct',
      'QtFontFallbacksCacheKey': '_qt_font_fallbacks_cache_key',
      'QtFontSize': '_qt_font_size',
      'QtFontStyle': '_qt_font_style',
      'RadialGradientValues': '_radial_gradient_values',
      'qfixed2d': '_qfixed2d',
      'quint24': '_quint24',
      'QBrushDataPointerDeleter': '_q_brush_data_pointer_deleter',
      'QColorTransferTable': '_q_color_transfer_table',
      'QGenericUnixThemePrivate': '_q_generic_unix_theme_private',
      'QGridLayoutRowData': '_q_grid_layout_row_data',
      'QPageRangesPrivate': '_q_page_ranges_private',
      'QRhiGles2NativeHandles': '_q_rhi_gles2_native_handles',
      'QRhiMetalCommandBufferNativeHandles': '_q_rhi_metal_command_buffer_native_handles',
      'QRhiMetalInitParams': '_q_rhi_metal_init_params',
      'QRhiMetalNativeHandles': '_q_rhi_metal_native_handles',
      'QRhiNullInitParams': '_q_rhi_null_init_params',
      'QRhiNullNativeHandles': '_q_rhi_null_native_handles',
      'QRhiVertexInputLayout': '_q_rhi_vertex_input_layout',
      'QRhiVulkanCommandBufferNativeHandles': '_q_rhi_vulkan_command_buffer_native_handles',
      'QRhiVulkanInitParams': '_q_rhi_vulkan_init_params',
      'QRhiVulkanNativeHandles': '_q_rhi_vulkan_native_handles',
      'QRhiVulkanQueueSubmitParams': '_q_rhi_vulkan_queue_submit_params',
      'QRhiVulkanRenderPassNativeHandles': '_q_rhi_vulkan_render_pass_native_handles',
      'QScriptItem': '_q_script_item',
      'QVarLengthGlyphLayoutArray': '_q_var_length_glyph_layout_array',
      'QVectorPathConverter': '_q_vector_path_converter',
      'QVulkanAdapter': '_q_vulkan_adapter',
      'QWindowSystemEventHandler': '_q_window_system_event_handler',
      'QAccessibleViewportInterface': '_q_accessible_viewport_interface',
      'QColorTrc': '_q_color_trc',
      'QColorVector': '_q_color_vector',
      'QEdidParser': '_q_edid_parser',
      'QFixedPoint': '_q_fixed_point',
      'QOpenGLExtensionMatcher': '_q_open_g_l_extension_matcher',
      'QOpenGLProgramBinaryCache': '_q_open_g_l_program_binary_cache',
      'QPathVertex': '_q_path_vertex',
      'QRhiBufferData': '_q_rhi_buffer_data',
      'QRhiPipelineCacheDataReader': '_q_rhi_pipeline_cache_data_reader',
      'QRhiTextureCopyDescription': '_q_rhi_texture_copy_description',
      'QShaderCode': '_q_shader_code',
      'QX11Info': '_q_x11_info',
      'QAccessibleActionInterface': '_q_accessible_action_interface',
      'QAccessibleEditableTextInterface': '_q_accessible_editable_text_interface',
      'QColor': '_q_color',
      'QColorCLUT': '_q_color_c_l_u_t',
      'QColorMatrix': '_q_color_matrix',
      'QColorTrcLut': '_q_color_trc_lut',
      'QFixedSize': '_q_fixed_size',
      'QGenericPluginFactory': '_q_generic_plugin_factory',
      'QGnomeThemePrivate': '_q_gnome_theme_private',
      'QIconDirInfo': '_q_icon_dir_info',
      'QIconLoader': '_q_icon_loader',
      'QIconTheme': '_q_icon_theme',
      'QPageRanges': '_q_page_ranges',
      'QPageSize': '_q_page_size',
      'QPdfPage': '_q_pdf_page',
      'QPlatformDragQtResponse': '_q_platform_drag_qt_response',
      'QPlatformInputContextFactory': '_q_platform_input_context_factory',
      'QPlatformIntegrationFactory': '_q_platform_integration_factory',
      'QPlatformThemeFactory': '_q_platform_theme_factory',
      'QPolygon': '_q_polygon',
      'QUndoCommand': '_q_undo_command',
      'QtFontFamily': '_qt_font_family',
      'QCmyk32': '_q_cmyk32',
      'QColorTransform': '_q_color_transform',
      'QGridLayoutItem': '_q_grid_layout_item',
      'QPageLayout': '_q_page_layout',
      'QPolygonF': '_q_polygon_f',
      'QtFontFoundry': '_qt_font_foundry',
      'QAccessibilityHints': '_q_accessibility_hints',
      'QAccessibleBridgePlugin': '_q_accessible_bridge_plugin',
      'QAccessiblePlugin': '_q_accessible_plugin',
      'QAccessibleValueInterface': '_q_accessible_value_interface',
      'QApplicationStateChangeEvent': '_q_application_state_change_event',
      'QCloseEvent': '_q_close_event',
      'QColorDialogOptions': '_q_color_dialog_options',
      'QColorSpace': '_q_color_space',
      'QColorTransformPrivate': '_q_color_transform_private',
      'QDesktopServices': '_q_desktop_services',
      'QDragLeaveEvent': '_q_drag_leave_event',
      'QDragPrivate': '_q_drag_private',
      'QDropEvent': '_q_drop_event',
      'QFocusEvent': '_q_focus_event',
      'QFontDialogOptions': '_q_font_dialog_options',
      'QFontVariableAxis': '_q_font_variable_axis',
      'QGenericPlugin': '_q_generic_plugin',
      'QGradient': '_q_gradient',
      'QHelpEvent': '_q_help_event',
      'QHideEvent': '_q_hide_event',
      'QIconDragEvent': '_q_icon_drag_event',
      'QIconEnginePlugin': '_q_icon_engine_plugin',
      'QImageIOPlugin': '_q_image_i_o_plugin',
      'QInputDevice': '_q_input_device',
      'QInputDevicePrivate': '_q_input_device_private',
      'QInputDeviceManager': '_q_input_device_manager',
      'QInputMethodEvent': '_q_input_method_event',
      'QInputMethodQueryEvent': '_q_input_method_query_event',
      'QInternalMimeData': '_q_internal_mime_data',
      'QKeySequence': '_q_key_sequence',
      'QLayoutPolicy': '_q_layout_policy',
      'QMoveEvent': '_q_move_event',
      'QOpenGLConfig': '_q_open_g_l_config',
      'QOpenGLContextGroup': '_q_open_g_l_context_group',
      'QPixelFormat': '_q_pixel_format',
      'QPlatformBackingStoreRhiConfig': '_q_platform_backing_store_rhi_config',
      'QPlatformInputContextPlugin': '_q_platform_input_context_plugin',
      'QPlatformInputContextPrivate': '_q_platform_input_context_private',
      'QPlatformIntegrationPlugin': '_q_platform_integration_plugin',
      'QPlatformServiceColorPicker': '_q_platform_service_color_picker',
      'QPlatformSurfaceEvent': '_q_platform_surface_event',
      'QPlatformThemePlugin': '_q_platform_theme_plugin',
      'QPointingDeviceUniqueId': '_q_pointing_device_unique_id',
      'QResizeEvent': '_q_resize_event',
      'QScreenPrivate': '_q_screen_private',
      'QScrollEvent': '_q_scroll_event',
      'QScrollPrepareEvent': '_q_scroll_prepare_event',
      'QSessionManagerPrivate': '_q_session_manager_private',
      'QShaderDescription': '_q_shader_description',
      'QShowEvent': '_q_show_event',
      'QStandardItemData': '_q_standard_item_data',
      'QStatusTipEvent': '_q_status_tip_event',
      'QStyleHints': '_q_style_hints',
      'QSurface': '_q_surface',
      'QTextureFileHandler': '_q_texture_file_handler',
      'QTextureFileReader': '_q_texture_file_reader',
      'QToolBarChangeEvent': '_q_tool_bar_change_event',
      'QUndoStack': '_q_undo_stack',
      'QUtiMimeConverter': '_q_uti_mime_converter',
      'QValidator': '_q_validator',
      'QWhatsThisClickedEvent': '_q_whats_this_clicked_event',
      'QWindowStateChangeEvent': '_q_window_state_change_event',
      'QWindowsMimeConverter': '_q_windows_mime_converter',
      'QAbstractLayoutStyleInfo': '_q_abstract_layout_style_info',
      'QAccessibilityHintsPrivate': '_q_accessibility_hints_private',
      'QAstcHandler': '_q_astc_handler',
      'QTransform': '_q_transform',
      'QFont': '_q_font',
      'QRegion': '_q_region',
      'QFontInfo': '_q_font_info',
      'QFontDatabase': '_q_font_database',
      'QImageIOHandler': '_q_image_i_o_handler',
      'QImageReader': '_q_image_reader',
      'QPaintDevice': '_q_paint_device',
      'QImage': '_q_image',
      'QBrush': '_q_brush',
      'QImageWriter': '_q_image_writer',
      'QPainterPath': '_q_painter_path',
      'QPen': '_q_pen',
      'QRawFont': '_q_raw_font',
      'QGlyphRun': '_q_glyph_run',
      'QStaticText': '_q_static_text',
      'QFontPrivate': '_q_font_private',
      'QPicture': '_q_picture',
      'QPixmap': '_q_pixmap',
      'QBitmap': '_q_bitmap',
      'QPainter': '_q_painter',
      'QPlatformPixmap': '_q_platform_pixmap',
      'QColorSpacePrivate': '_q_color_space_private',
      'QConicalGradient': '_q_conical_gradient',
      'QDBusListener': '_q_d_bus_listener',
      'QDBusMenuRegistrarInterface': '_q_d_bus_menu_registrar_interface',
      'QDoubleValidator': '_q_double_validator',
      'QDragMoveEvent': '_q_drag_move_event',
      'QInputDeviceManagerPrivate': '_q_input_device_manager_private',
      'QInputEvent': '_q_input_event',
      'QIntValidator': '_q_int_validator',
      'QKeySequencePrivate': '_q_key_sequence_private',
      'QKtxHandler': '_q_ktx_handler',
      'QLinearGradient': '_q_linear_gradient',
      'QPAEventDispatcherGlibPrivate': '_q_p_a_event_dispatcher_glib_private',
      'QPdfOutputIntent': '_q_pdf_output_intent',
      'QPkmHandler': '_q_pkm_handler',
      'QPlatformGraphicsBuffer': '_q_platform_graphics_buffer',
      'QPlatformSurface': '_q_platform_surface',
      'QRadialGradient': '_q_radial_gradient',
      'QRegularExpressionValidator': '_q_regular_expression_validator',
      'QShader': '_q_shader',
      'QShaderKey': '_q_shader_key',
      'QShaderDescriptionPrivate': '_q_shader_description_private',
      'QShortcut': '_q_shortcut',
      'QSpiObjectReference': '_q_spi_object_reference',
      'QSurfaceFormat': '_q_surface_format',
      'QUndoGroup': '_q_undo_group',
      'QXdgNotificationInterface': '_q_xdg_notification_interface',
      'QBezier': '_q_bezier',
      'QBmpHandler': '_q_bmp_handler',
      'QClipData': '_q_clip_data',
      'QClipboard': '_q_clipboard',
      'QColrPaintGraphRenderer': '_q_colr_paint_graph_renderer',
      'QContextMenuEvent': '_q_context_menu_event',
      'QCursorData': '_q_cursor_data',
      'QDistanceFieldData': '_q_distance_field_data',
      'QDrag': '_q_drag',
      'QDragEnterEvent': '_q_drag_enter_event',
      'QExposeEvent': '_q_expose_event',
      'QFileOpenEvent': '_q_file_open_event',
      'QFontDatabasePrivate': '_q_font_database_private',
      'QFontMetrics': '_q_font_metrics',
      'QGlyphRunPrivate': '_q_glyph_run_private',
      'QGnomePortalInterface': '_q_gnome_portal_interface',
      'QGridLayoutEngine': '_q_grid_layout_engine',
      'QImageData': '_q_image_data',
      'QImagePixmapCleanupHooks': '_q_image_pixmap_cleanup_hooks',
      'QInputMethod': '_q_input_method',
      'QKeyEvent': '_q_key_event',
      'QVector4D': '_q_vector4_d',
      'QVector3D': '_q_vector3_d',
      'QQuaternion': '_q_quaternion',
      'QMatrix4x4': '_q_matrix4x4',
      'QVector2D': '_q_vector2_d',
      'QMovie': '_q_movie',
      'QPAEventDispatcherGlib': '_q_p_a_event_dispatcher_glib',
      'QPagedPaintDevice': '_q_paged_paint_device',
      'QPagedPaintDevicePrivate': '_q_paged_paint_device_private',
      'QPaintEvent': '_q_paint_event',
      'QPainterClipInfo': '_q_painter_clip_info',
      'QPainterPathPrivate': '_q_painter_path_private',
      'QPainterPathStroker': '_q_painter_path_stroker',
      'QPainterState': '_q_painter_state',
      'QPainterStateGuard': '_q_painter_state_guard',
      'QPalette': '_q_palette',
      'QPathSegments': '_q_path_segments',
      'QPenPrivate': '_q_pen_private',
      'QPixmapCache': '_q_pixmap_cache',
      'QPixmapCacheEntry': '_q_pixmap_cache_entry',
      'QPlatformCursorImage': '_q_platform_cursor_image',
      'QPlatformSharedGraphicsCache': '_q_platform_shared_graphics_cache',
      'QPngHandler': '_q_png_handler',
      'QPpmHandler': '_q_ppm_handler',
      'QRasterBuffer': '_q_raster_buffer',
      'QRasterPlatformPixmap': '_q_raster_platform_pixmap',
      'QRasterizer': '_q_rasterizer',
      'QRhiGles2InitParams': '_q_rhi_gles2_init_params',
      'QRhiShaderStage': '_q_rhi_shader_stage',
      'QRhiTextureSubresourceUploadDescription': '_q_rhi_texture_subresource_upload_description',
      'QShaderPrivate': '_q_shader_private',
      'QShortcutEvent': '_q_shortcut_event',
      'QSpiDBusCache': '_q_spi_d_bus_cache',
      'QStaticTextPrivate': '_q_static_text_private',
      'QStrokerOps': '_q_stroker_ops',
      'QSupportedWritingSystems': '_q_supported_writing_systems',
      'QTextFormat': '_q_text_format',
      'QTextureFileData': '_q_texture_file_data',
      'QUnixEventDispatcherQPA': '_q_unix_event_dispatcher_q_p_a',
      'QWingedEdge': '_q_winged_edge',
      'QXbmHandler': '_q_xbm_handler',
      'QXpmHandler': '_q_xpm_handler',
      'glyph_metrics_t': '_glyph_metrics_t',
      'QDragManager': '_q_drag_manager',
      'QEventPoint': '_q_event_point',
      'QPointerEvent': '_q_pointer_event',
      'QPointingDevice': '_q_pointing_device',
      'QTouchEvent': '_q_touch_event',
      'QPointingDevicePrivate': '_q_pointing_device_private',
      'QFileDialogOptions': '_q_file_dialog_options',
      'QFontEngine': '_q_font_engine',
      'QFontEngineGlyphCache': '_q_font_engine_glyph_cache',
      'QFontMetricsF': '_q_font_metrics_f',
      'QInputControl': '_q_input_control',
      'QInputMethodPrivate': '_q_input_method_private',
      'QKeyMapper': '_q_key_mapper',
      'QPalettePrivate': '_q_palette_private',
      'QPathClipper': '_q_path_clipper',
      'QPdfWriter': '_q_pdf_writer',
      'QPlatformClipboard': '_q_platform_clipboard',
      'QPlatformDrag': '_q_platform_drag',
      'QPlatformInputContext': '_q_platform_input_context',
      'QPlatformKeyMapper': '_q_platform_key_mapper',
      'QRasterPaintEngineState': '_q_raster_paint_engine_state',
      'QRhiTextureUploadEntry': '_q_rhi_texture_upload_entry',
      'QShortcutMap': '_q_shortcut_map',
      'QSpiApplicationAdaptor': '_q_spi_application_adaptor',
      'QStroker': '_q_stroker',
      'QTextBlockFormat': '_q_text_block_format',
      'QTextCharFormat': '_q_text_char_format',
      'QTextFormatCollection': '_q_text_format_collection',
      'QTextFrameFormat': '_q_text_frame_format',
      'QTextListFormat': '_q_text_list_format',
      'QBlittable': '_q_blittable',
      'QDashStroker': '_q_dash_stroker',
      'QDistanceField': '_q_distance_field',
      'QEventPointPrivate': '_q_event_point_private',
      'QFontCache': '_q_font_cache',
      'QFontEngineMulti': '_q_font_engine_multi',
      'QFontSubset': '_q_font_subset',
      'QMutableTouchEvent': '_q_mutable_touch_event',
      'QPlatformFontDatabase': '_q_platform_font_database',
      'QRawFontPrivate': '_q_raw_font_private',
      'QRhiTextureUploadDescription': '_q_rhi_texture_upload_description',
      'QShortcutPrivate': '_q_shortcut_private',
      'QSinglePointEvent': '_q_single_point_event',
      'QStaticTextItem': '_q_static_text_item',
      'QTextImageFormat': '_q_text_image_format',
      'QTextItemInt': '_q_text_item_int',
      'QTextTableCellFormat': '_q_text_table_cell_format',
      'QTextTableFormat': '_q_text_table_format',
      'QTextureGlyphCache': '_q_texture_glyph_cache',
      'QAbstractFileIconProvider': '_q_abstract_file_icon_provider',
      'QAbstractFileIconProviderPrivate': '_q_abstract_file_icon_provider_private',
      'QTextDocument': '_q_text_document',
      'QTextBlock': '_q_text_block',
      'QTextEngine': '_q_text_engine',
      'QTextInlineObject': '_q_text_inline_object',
      'QTextLayout': '_q_text_layout',
      'QTextObjectPrivate': '_q_text_object_private',
      'QTextFramePrivate': '_q_text_frame_private',
      'QTextObject': '_q_text_object',
      'QTextFrame': '_q_text_frame',
      'QAbstractTextDocumentLayout': '_q_abstract_text_document_layout',
      'QTextDocumentPrivate': '_q_text_document_private',
      'QTextCursor': '_q_text_cursor',
      'QTextTable': '_q_text_table',
      'QAbstractTextDocumentLayoutPrivate': '_q_abstract_text_document_layout_private',
      'QScriptLine': '_q_script_line',
      'QTextCursorPrivate': '_q_text_cursor_private',
      'QTextDocumentFragment': '_q_text_document_fragment',
      'QEnterEvent': '_q_enter_event',
      'QExtendedInformation': '_q_extended_information',
      'QFileSystemModelPrivate': '_q_file_system_model_private',
      'QFreeTypeFontDatabase': '_q_free_type_font_database',
      'QHoverEvent': '_q_hover_event',
      'QImageTextureGlyphCache': '_q_image_texture_glyph_cache',
      'QMouseEvent': '_q_mouse_event',
      'QMutableSinglePointEvent': '_q_mutable_single_point_event',
      'QNativeGestureEvent': '_q_native_gesture_event',
      'QPaintEngine': '_q_paint_engine',
      'QPaintEnginePrivate': '_q_paint_engine_private',
      'QPlatformTheme': '_q_platform_theme',
      'QTabletEvent': '_q_tablet_event',
      'QWheelEvent': '_q_wheel_event',
      'QAccessibleInterface': '_q_accessible_interface',
      'QAccessible': '_q_accessible',
      'QAccessibleEvent': '_q_accessible_event',
      'QScreen': '_q_screen',
      'QCursor': '_q_cursor',
      'QWindow': '_q_window',
      'QIcon': '_q_icon',
      'QIconEngine': '_q_icon_engine',
      'QPlatformScreen': '_q_platform_screen',
      'QVulkanInstance': '_q_vulkan_instance',
      'QWindowPrivate': '_q_window_private',
      'QFileInfoGatherer': '_q_file_info_gatherer',
      'QFileSystemModel': '_q_file_system_model',
      'QFontEngineBox': '_q_font_engine_box',
      'QFontconfigDatabase': '_q_fontconfig_database',
      'QGenericUnixTheme': '_q_generic_unix_theme',
      'QPaintEngineExPrivate': '_q_paint_engine_ex_private',
      'QPainterPrivate': '_q_painter_private',
      'QPdfEnginePrivate': '_q_pdf_engine_private',
      'QPicturePaintEngine': '_q_picture_paint_engine',
      'QStackTextEngine': '_q_stack_text_engine',
      'QStyleHintsPrivate': '_q_style_hints_private',
      'QSyntaxHighlighter': '_q_syntax_highlighter',
      'QTextBlockGroupPrivate': '_q_text_block_group_private',
      'QTextCopyHelper': '_q_text_copy_helper',
      'QTextDocumentFragmentPrivate': '_q_text_document_fragment_private',
      'QTextDocumentWriter': '_q_text_document_writer',
      'QTextFragment': '_q_text_fragment',
      'QTextHtmlParser': '_q_text_html_parser',
      'QTextLine': '_q_text_line',
      'QTextLineItemIterator': '_q_text_line_item_iterator',
      'QTextMarkdownImporter': '_q_text_markdown_importer',
      'QTextObjectInterface': '_q_text_object_interface',
      'QTextTableCell': '_q_text_table_cell',
      'QTextTablePrivate': '_q_text_table_private',
      'QAccessibleAnnouncementEvent': '_q_accessible_announcement_event',
      'QAccessibleAttributesInterface': '_q_accessible_attributes_interface',
      'QAccessibleBridge': '_q_accessible_bridge',
      'QAccessibleCache': '_q_accessible_cache',
      'QAccessibleObject': '_q_accessible_object',
      'QAccessibleObjectDestroyedEvent': '_q_accessible_object_destroyed_event',
      'QAccessibleSelectionInterface': '_q_accessible_selection_interface',
      'QAccessibleStateChangeEvent': '_q_accessible_state_change_event',
      'QAccessibleTableModelChangeEvent': '_q_accessible_table_model_change_event',
      'QAccessibleTextCursorEvent': '_q_accessible_text_cursor_event',
      'QAccessibleTextInterface': '_q_accessible_text_interface',
      'QAccessibleValueChangeEvent': '_q_accessible_value_change_event',
      'QAction': '_q_action',
      'QActionGroupPrivate': '_q_action_group_private',
      'QActionGroup': '_q_action_group',
      'QActionPrivate': '_q_action_private',
      'QBackingStore': '_q_backing_store',
      'QBackingStoreRhiSupport': '_q_backing_store_rhi_support',
      'QBasicDrag': '_q_basic_drag',
      'QChildWindowEvent': '_q_child_window_event',
      'QFontIconEngine': '_q_font_icon_engine',
      'QGnomeTheme': '_q_gnome_theme',
      'QHighDpiScaling': '_q_high_dpi_scaling',
      'QIconLoaderEngine': '_q_icon_loader_engine',
      'QIconLoaderEngineEntry': '_q_icon_loader_engine_entry',
      'QIconPrivate': '_q_icon_private',
      'QKdeTheme': '_q_kde_theme',
      'QMutableEventPoint': '_q_mutable_event_point',
      'QOffscreenSurface': '_q_offscreen_surface',
      'QOpenGLContext': '_q_open_g_l_context',
      'QPaintDeviceWindowPrivate': '_q_paint_device_window_private',
      'QPaintEngineEx': '_q_paint_engine_ex',
      'QVectorPath': '_q_vector_path',
      'QPdfEngine': '_q_pdf_engine',
      'QPixmapIconEngineEntry': '_q_pixmap_icon_engine_entry',
      'QPlatformAccessibility': '_q_platform_accessibility',
      'QPlatformCursor': '_q_platform_cursor',
      'QPlatformDialogHelper': '_q_platform_dialog_helper',
      'QPlatformMenu': '_q_platform_menu',
      'QPlatformMenuItem': '_q_platform_menu_item',
      'QPlatformPlaceholderScreen': '_q_platform_placeholder_screen',
      'QPlatformServices': '_q_platform_services',
      'QPlatformVulkanInstance': '_q_platform_vulkan_instance',
      'QPlatformWindow': '_q_platform_window',
      'QProxyIconEngine': '_q_proxy_icon_engine',
      'QRhiReadbackDescription': '_q_rhi_readback_description',
      'QRhiResource': '_q_rhi_resource',
      'QRhiTexture': '_q_rhi_texture',
      'QRhiBuffer': '_q_rhi_buffer',
      'QRhiRenderBuffer': '_q_rhi_render_buffer',
      'QRhiRenderPassDescriptor': '_q_rhi_render_pass_descriptor',
      'QRhiSampler': '_q_rhi_sampler',
      'QRhiShaderResourceBinding': '_q_rhi_shader_resource_binding',
      'QRhiShaderResourceBindings': '_q_rhi_shader_resource_bindings',
      'QRhiColorAttachment': '_q_rhi_color_attachment',
      'QRhiTextureRenderTargetDescription': '_q_rhi_texture_render_target_description',
      'QRhiComputePipeline': '_q_rhi_compute_pipeline',
      'QRhiGraphicsPipeline': '_q_rhi_graphics_pipeline',
      'QRhiRenderTarget': '_q_rhi_render_target',
      'QRhiResourceUpdateBatch': '_q_rhi_resource_update_batch',
      'QRhiCommandBuffer': '_q_rhi_command_buffer',
      'QRhiTextureRenderTarget': '_q_rhi_texture_render_target',
      'QRhi': '_q_rhi',
      'QRhiImplementation': '_q_rhi_implementation',
      'QRhiShadingRateMap': '_q_rhi_shading_rate_map',
      'QRhiSwapChain': '_q_rhi_swap_chain',
      'QScreenOrientationChangeEvent': '_q_screen_orientation_change_event',
      'QStandardItem': '_q_standard_item',
      'QStandardItemModelPrivate': '_q_standard_item_model_private',
      'QStandardItemModel': '_q_standard_item_model',
      'QStandardItemPrivate': '_q_standard_item_private',
      'QTestFontEngine': '_q_test_font_engine',
      'QTextBlockGroup': '_q_text_block_group',
      'QTextDocumentLayout': '_q_text_document_layout',
      'QTextHtmlExporter': '_q_text_html_exporter',
      'QTextHtmlImporter': '_q_text_html_importer',
      'QTextHtmlParserNode': '_q_text_html_parser_node',
      'QTextImageHandler': '_q_text_image_handler',
      'QTextOdfWriter': '_q_text_odf_writer',
      'QVulkanWindow': '_q_vulkan_window',
      'QVulkanWindowPrivate': '_q_vulkan_window_private',
      'QWindowSystemInterface': '_q_window_system_interface',
      'QWindowSystemInterfacePrivate': '_q_window_system_interface_private',
      'PixmapEntry': '_pixmap_entry',
      'QAccessibleApplication': '_q_accessible_application',
      'QAccessibleTableInterface': '_q_accessible_table_interface',
      'QAccessibleTextInsertEvent': '_q_accessible_text_insert_event',
      'QAccessibleTextRemoveEvent': '_q_accessible_text_remove_event',
      'QAccessibleTextSelectionEvent': '_q_accessible_text_selection_event',
      'QAccessibleTextUpdateEvent': '_q_accessible_text_update_event',
      'QActionEvent': '_q_action_event',
      'QBackingStoreRhiSupportWindowWatcher': '_q_backing_store_rhi_support_window_watcher',
      'QBasicPlatformVulkanInstance': '_q_basic_platform_vulkan_instance',
      'QBlittablePlatformPixmap': '_q_blittable_platform_pixmap',
      'QCosmeticStroker': '_q_cosmetic_stroker',
      'QDBusPlatformMenuItem': '_q_d_bus_platform_menu_item',
      'QDashedStrokeProcessor': '_q_dashed_stroke_processor',
      'QDesktopUnixServices': '_q_desktop_unix_services',
      'QEmulationPaintEngine': '_q_emulation_paint_engine',
      'QGles2Buffer': '_q_gles2_buffer',
      'QGles2CommandBuffer': '_q_gles2_command_buffer',
      'QGles2ComputePipeline': '_q_gles2_compute_pipeline',
      'QGles2GraphicsPipeline': '_q_gles2_graphics_pipeline',
      'QGles2RenderBuffer': '_q_gles2_render_buffer',
      'QGles2RenderPassDescriptor': '_q_gles2_render_pass_descriptor',
      'QGles2RenderTargetData': '_q_gles2_render_target_data',
      'QGles2Sampler': '_q_gles2_sampler',
      'QGles2ShaderResourceBindings': '_q_gles2_shader_resource_bindings',
      'QGles2Texture': '_q_gles2_texture',
      'QGles2TextureRenderTarget': '_q_gles2_texture_render_target',
      'QGraphicsFrameCapture': '_q_graphics_frame_capture',
      'QGraphicsFrameCapturePrivate': '_q_graphics_frame_capture_private',
      'QMessageDialogOptions': '_q_message_dialog_options',
      'QMetalBuffer': '_q_metal_buffer',
      'QMetalCommandBuffer': '_q_metal_command_buffer',
      'QMetalComputePipeline': '_q_metal_compute_pipeline',
      'QMetalRenderBuffer': '_q_metal_render_buffer',
      'QMetalRenderPassDescriptor': '_q_metal_render_pass_descriptor',
      'QMetalSampler': '_q_metal_sampler',
      'QMetalShaderResourceBindings': '_q_metal_shader_resource_bindings',
      'QMetalShadingRateMap': '_q_metal_shading_rate_map',
      'QMetalSwapChain': '_q_metal_swap_chain',
      'QMetalTexture': '_q_metal_texture',
      'QMetalTextureRenderTarget': '_q_metal_texture_render_target',
      'QNullBuffer': '_q_null_buffer',
      'QNullCommandBuffer': '_q_null_command_buffer',
      'QNullComputePipeline': '_q_null_compute_pipeline',
      'QNullGraphicsPipeline': '_q_null_graphics_pipeline',
      'QNullRenderBuffer': '_q_null_render_buffer',
      'QNullRenderPassDescriptor': '_q_null_render_pass_descriptor',
      'QNullRenderTargetData': '_q_null_render_target_data',
      'QNullSampler': '_q_null_sampler',
      'QNullShaderResourceBindings': '_q_null_shader_resource_bindings',
      'QNullSwapChain': '_q_null_swap_chain',
      'QNullTexture': '_q_null_texture',
      'QNullTextureRenderTarget': '_q_null_texture_render_target',
      'QOffscreenSurfacePrivate': '_q_offscreen_surface_private',
      'QOpenGLContextGroupPrivate': '_q_open_g_l_context_group_private',
      'QOpenGLFunctionsPrivate': '_q_open_g_l_functions_private',
      'QOpenGLProgramBinarySupportCheckWrapper': '_q_open_g_l_program_binary_support_check_wrapper',
      'QOpenGLSharedResource': '_q_open_g_l_shared_resource',
      'QOutlineMapper': '_q_outline_mapper',
      'QPaintDeviceWindow': '_q_paint_device_window',
      'QPixmapIconEngine': '_q_pixmap_icon_engine',
      'QPlatformColorDialogHelper': '_q_platform_color_dialog_helper',
      'QPlatformFileDialogHelper': '_q_platform_file_dialog_helper',
      'QPlatformFontDialogHelper': '_q_platform_font_dialog_helper',
      'QPlatformIntegration': '_q_platform_integration',
      'QPlatformMenuBar': '_q_platform_menu_bar',
      'QPlatformNativeInterface': '_q_platform_native_interface',
      'QPlatformOffscreenSurface': '_q_platform_offscreen_surface',
      'QPlatformOpenGLContext': '_q_platform_open_g_l_context',
      'QPlatformSystemTrayIcon': '_q_platform_system_tray_icon',
      'QPlatformTextureList': '_q_platform_texture_list',
      'QSpanData': '_q_span_data',
      'QRasterPaintEnginePrivate': '_q_raster_paint_engine_private',
      'QRasterPaintEngine': '_q_raster_paint_engine',
      'QRhiPassResourceTracker': '_q_rhi_pass_resource_tracker',
      'QRhiResourceUpdateBatchPrivate': '_q_rhi_resource_update_batch_private',
      'QRhiSwapChainRenderTarget': '_q_rhi_swap_chain_render_target',
      'QSimpleDrag': '_q_simple_drag',
      'QSpiAccessibleBridge': '_q_spi_accessible_bridge',
      'QTextList': '_q_text_list',
      'QThemeIconEngine': '_q_theme_icon_engine',
      'QTriangulatingStroker': '_q_triangulating_stroker',
      'QUndoStackPrivate': '_q_undo_stack_private',
      'QVkBuffer': '_q_vk_buffer',
      'QVkCommandBuffer': '_q_vk_command_buffer',
      'QVkComputePipeline': '_q_vk_compute_pipeline',
      'QVkGraphicsPipeline': '_q_vk_graphics_pipeline',
      'QVkRenderBuffer': '_q_vk_render_buffer',
      'QVkRenderPassDescriptor': '_q_vk_render_pass_descriptor',
      'QVkSampler': '_q_vk_sampler',
      'QVkShaderResourceBindings': '_q_vk_shader_resource_bindings',
      'QVkShadingRateMap': '_q_vk_shading_rate_map',
      'QVkSwapChain': '_q_vk_swap_chain',
      'QVkTexture': '_q_vk_texture',
      'QVkTextureRenderTarget': '_q_vk_texture_render_target',
      'ScalableEntry': '_scalable_entry',
      'QAbstractFileIconEngine': '_q_abstract_file_icon_engine',
      'QBlitterPaintEngine': '_q_blitter_paint_engine',
      'QDBusMenuBar': '_q_d_bus_menu_bar',
      'QDBusMenuItem': '_q_d_bus_menu_item',
      'QDBusPlatformMenu': '_q_d_bus_platform_menu',
      'QDBusTrayIcon': '_q_d_bus_tray_icon',
      'QGles2SwapChainRenderTarget': '_q_gles2_swap_chain_render_target',
      'QGraphicsFrameCaptureMetal': '_q_graphics_frame_capture_metal',
      'QMetalGraphicsPipeline': '_q_metal_graphics_pipeline',
      'QMetalSwapChainRenderTarget': '_q_metal_swap_chain_render_target',
      'QNullSwapChainRenderTarget': '_q_null_swap_chain_render_target',
      'QOpenGLContextPrivate': '_q_open_g_l_context_private',
      'QOpenGLExtraFunctionsPrivate': '_q_open_g_l_extra_functions_private',
      'QOpenGLFunctions': '_q_open_g_l_functions',
      'QOpenGLMultiGroupSharedResource': '_q_open_g_l_multi_group_shared_resource',
      'QOpenGLProgramBinarySupportCheck': '_q_open_g_l_program_binary_support_check',
      'QOpenGLSharedResourceGuard': '_q_open_g_l_shared_resource_guard',
      'QPlatformBackingStore': '_q_platform_backing_store',
      'QPlatformMessageDialogHelper': '_q_platform_message_dialog_helper',
      'QRasterWindow': '_q_raster_window',
      'QRhiGles2': '_q_rhi_gles2',
      'QRhiMetal': '_q_rhi_metal',
      'QRhiNull': '_q_rhi_null',
      'QRhiVulkan': '_q_rhi_vulkan',
      'QTextMarkdownWriter': '_q_text_markdown_writer',
      'QVkSwapChainRenderTarget': '_q_vk_swap_chain_render_target',
      'QBackingStoreDefaultCompositor': '_q_backing_store_default_compositor',
      'QDBusMenuConnection': '_q_d_bus_menu_connection',
      'QDBusMenuLayoutItem': '_q_d_bus_menu_layout_item',
      'QGles2SwapChain': '_q_gles2_swap_chain',
      'QGles2SwapChainTimestamps': '_q_gles2_swap_chain_timestamps',
      'QOpenGLExtensionsPrivate': '_q_open_g_l_extensions_private',
      'QOpenGLExtraFunctions': '_q_open_g_l_extra_functions',
      'QRasterBackingStore': '_q_raster_backing_store',
      'QShapedPixmapWindow': '_q_shaped_pixmap_window',
      'QStatusNotifierItemAdaptor': '_q_status_notifier_item_adaptor',
      'QDBusMenuAdaptor': '_q_d_bus_menu_adaptor',
      'QOpenGLExtensions': '_q_open_g_l_extensions',
      'QRhiBackingStore': '_q_rhi_backing_store',
      'QGuiApplicationPrivate': '_q_gui_application_private',
      'QGuiApplication': '_q_gui_application',
      'QSessionManager': '_q_session_manager',
      'QPlatformSessionManager': '_q_platform_session_manager',
      'QDBusMenuEventList': '_q_d_bus_menu_event',
      'QDBusMenuItemKeysList': '_q_d_bus_menu_item_keys',
      'QSpiAccessibleCacheArray': '_q_spi_accessible_cache_item',
      'QXdgDBusImageVector': '_q_xdg_d_bus_image_struct',
      'QWindowList': '_q_window',
      'QDBusMenuItemList': '_q_d_bus_menu_item',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QCss', 'QGuiSvg', 'QImageReaderWriterHelpers', 'QImageScale', 'QNativeInterface', 'QPdf', 'QTest',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtGui import QDBusMenuItemList'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
