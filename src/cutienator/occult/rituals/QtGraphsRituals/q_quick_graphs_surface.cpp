//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphssurface_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphssurface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGraphs/qsurface3dseries.h>
#include <QtCore/qpoint.h>
#include <QtGraphs/qabstract3dseries.h>
#include <QtCore/qurl.h>
#include <QtGui/qvectornd.h>
#include <QtGraphs/qsurfacedataitem.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickGraphsSurface may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsSurface : QQuickGraphsSurface {
  using QQuickGraphsSurface::componentComplete;
  using QQuickGraphsSurface::synchData;
  using QQuickGraphsSurface::updateGraph;
  using QQuickGraphsSurface::calculateSceneScalingFactors;
  using QQuickGraphsSurface::toggleSliceGraph;
  using QQuickGraphsSurface::updateSingleHighlightColor;
  using QQuickGraphsSurface::updateLightStrength;
  using QQuickGraphsSurface::handleThemeTypeChange;
  using QQuickGraphsSurface::doPicking;
  using QQuickGraphsSurface::doRayPicking;
  using QQuickGraphsSurface::getSeriesMultiAxis;
  using QQuickGraphsSurface::createSliceView;
  using QQuickGraphsSurface::updateSliceItemLabel;
  using QQuickGraphsSurface::updateSelectionMode;
};

//  A QQuickGraphsSurface that Python can take functions over in. Every QQuickGraphsSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsSurfaceCall0)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall1)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall2)(const void *, int, bool, int *);
typedef void (*CuteQQuickGraphsSurfaceCall3)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall4)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall5)(const void *, bool, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall6)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall7)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall8)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall9)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall10)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall11)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall12)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall13)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall14)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall15)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall16)(const void *, int *);
typedef bool (*CuteQQuickGraphsSurfaceCall17)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsSurfaceCall18)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void * (*CuteQQuickGraphsSurfaceCall19)(const void *, QAbstract3DSeries *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall20)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall21)(const void *, const QString *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall22)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall23)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall24)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall25)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall26)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall27)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall28)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall29)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall30)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall31)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall32)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall33)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall34)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall35)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall36)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall37)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall38)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall39)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall40)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall41)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall42)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall43)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall44)(const void *, int, int *);
typedef int (*CuteQQuickGraphsSurfaceCall45)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall46)(const void *, int, int *);
typedef int (*CuteQQuickGraphsSurfaceCall47)(const void *, int *);
typedef int (*CuteQQuickGraphsSurfaceCall48)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall49)(const void *, int, int *);
typedef int (*CuteQQuickGraphsSurfaceCall50)(const void *, int *);
typedef int (*CuteQQuickGraphsSurfaceCall51)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall52)(const void *, int, int *);
typedef int (*CuteQQuickGraphsSurfaceCall53)(const void *, int *);
typedef bool (*CuteQQuickGraphsSurfaceCall54)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsSurfaceCall55)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall56)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall57)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall58)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall59)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsSurfaceCall60)(const void *, int *);
typedef void * (*CuteQQuickGraphsSurfaceCall61)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsSurfaceCall62)(const void *, int *);
typedef void * (*CuteQQuickGraphsSurfaceCall63)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall64)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsSurfaceCall65)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceCall66)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall67)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall68)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall69)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall70)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall71)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall72)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall73)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall74)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall75)(const void *, int *);
typedef const QVector3D * (*CuteQQuickGraphsSurfaceCall76)(const void *, QAbstract3DAxis *, const QVector3D *, int, int *);
typedef float (*CuteQQuickGraphsSurfaceCall77)(const void *, QAbstract3DAxis *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall78)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall79)(const void *, float, float, int *);
typedef void (*CuteQQuickGraphsSurfaceCall80)(const void *, bool, int *);
typedef void (*CuteQQuickGraphsSurfaceCall81)(const void *, QQuick3DRepeater *, const QColor *, int *);
typedef void * (*CuteQQuickGraphsSurfaceCall82)(const void *, int, int *);
typedef void (*CuteQQuickGraphsSurfaceCall83)(const void *, int *);
typedef bool (*CuteQQuickGraphsSurfaceCall84)(const void *, int *);
typedef void * (*CuteQQuickGraphsSurfaceCall85)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall86)(const void *, int *);
typedef void * (*CuteQQuickGraphsSurfaceCall87)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQQuickGraphsSurfaceCall88)(const void *, int *);
typedef const QRectF * (*CuteQQuickGraphsSurfaceCall89)(const void *, int *);
typedef bool (*CuteQQuickGraphsSurfaceCall90)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickGraphsSurfaceCall91)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsSurfaceCall92)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall93)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickGraphsSurfaceCall94)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsSurfaceCall95)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall96)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall97)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall98)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall99)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall100)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall101)(const void *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall102)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsSurfaceCall103)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsSurfaceCall104)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall105)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall106)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall107)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsSurfaceCall108)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsSurfaceCall109)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsSurfaceCall110)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsSurfaceCall111)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickGraphsSurfaceCall112)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickGraphsSurfaceCall113)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsSurfaceCall114)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceCall115)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceCall116)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceCall117)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceCall118)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsSurfaceCall119)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsSurface : public QQuickGraphsSurface {
public:
  using QQuickGraphsSurface::QQuickGraphsSurface;
  void *taken[120] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14clearSelectionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisRangeChangedBySenderEP7QObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7QObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySenderEbP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16adjustAxisRangesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleLightingModeChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9synchDataEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11updateGraphEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16toggleSliceGraphEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem26updateSingleHighlightColorEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateLightStrengthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem21handleThemeTypeChangeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9doPickingE7QPointF")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15createSliceViewEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3D")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObject")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7QObject")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySenderEP7QObject")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7QObject")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObject")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObject")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySenderEP7QObject")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySenderEP7QObject")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QObject")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySenderEP7QObject")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySenderEP7QObject")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QObject")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7QObject")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSeries")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13RenderingModeE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13renderingModeEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem21transparencyTechniqueEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13selectionModeEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13shadowQualityEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem15selectedElementEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14setMsaaSamplesEi")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem11msaaSamplesEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17removeCustomItemsEv")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedLabelIndexEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem12selectedAxisEv")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedCustomItemEv")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[64] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[65] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19handleWindowChangedEv")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22updateWindowParametersEv")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D13ShadowQualityE")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3D11ElementTypeE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleParentWidthChangeEv")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24handleParentHeightChangeEv")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAbstract3DAxisi")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15updateAxisRangeEff")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18updateAxisReversedEb")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepeater6QColor")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[90] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[91] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[93] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[94] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[102] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[103] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[107] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[108] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[109] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[110] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[111] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[113] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[114] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[115] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[116] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[117] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[118] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[119] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickGraphsSurface::clearSelection()
  void clearSelection() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall0 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::clearSelection();
  }

  //  void QQuickGraphsSurface::setSelectionMode(QtGraphs3D::SelectionFlags
  //      mode)
  void setSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall1 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall1>(taken[1]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::setSelectionMode(mode);
  }

  //  void QQuickGraphsSurface::handleAxisAutoAdjustRangeChangedInOrientati
  //      on(QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
  void handleAxisAutoAdjustRangeChangedInOrientation(
      QAbstract3DAxis::AxisOrientation orientation,
      bool autoAdjust) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall2 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall2>(taken[2]);
      call(this, static_cast<int>(orientation), autoAdjust, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleAxisAutoAdjustRangeChangedInOrientation(orientation, autoAdjust);
  }

  //  void QQuickGraphsSurface::handleAxisRangeChangedBySender(QObject
  //      *sender)
  void handleAxisRangeChangedBySender(QObject *sender) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall3 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall3>(taken[3]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleAxisRangeChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleSeriesVisibilityChangedBySender(QObject *sender) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall4 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall4>(taken[4]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(bool
  //      visible, QObject *sender)
  void handleItemLabelVisibleChangedBySender(
      bool visible,
      QObject *sender) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall5 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall5>(taken[5]);
      call(this, visible, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(visible, sender);
  }

  //  void QQuickGraphsSurface::adjustAxisRanges()
  void adjustAxisRanges() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall6 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::adjustAxisRanges();
  }

  //  void QQuickGraphsSurface::handleMultiAxisChanged(QAbstract3DAxis
  //      *axis)
  void handleMultiAxisChanged(QAbstract3DAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall7 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall7>(taken[7]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleMultiAxisChanged(axis);
  }

  //  void QQuickGraphsSurface::handleLightingModeChanged()
  void handleLightingModeChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall8 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleLightingModeChanged();
  }

  //  void QQuickGraphsSurface::componentComplete()
  void componentComplete() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall9 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::componentComplete();
  }

  //  void QQuickGraphsSurface::synchData()
  void synchData() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall10 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::synchData();
  }

  //  void QQuickGraphsSurface::updateGraph()
  void updateGraph() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall11 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::updateGraph();
  }

  //  void QQuickGraphsSurface::calculateSceneScalingFactors()
  void calculateSceneScalingFactors() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall12 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::calculateSceneScalingFactors();
  }

  //  void QQuickGraphsSurface::toggleSliceGraph()
  void toggleSliceGraph() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall13 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::toggleSliceGraph();
  }

  //  void QQuickGraphsSurface::updateSingleHighlightColor()
  void updateSingleHighlightColor() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall14 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::updateSingleHighlightColor();
  }

  //  void QQuickGraphsSurface::updateLightStrength()
  void updateLightStrength() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall15 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::updateLightStrength();
  }

  //  void QQuickGraphsSurface::handleThemeTypeChange()
  void handleThemeTypeChange() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall16 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleThemeTypeChange();
  }

  //  bool QQuickGraphsSurface::doPicking(QPointF position)
  bool doPicking(QPointF position) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall17 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall17>(taken[17]);
      bool given = call(this, &position, &handled);
      if (handled) return given;
    }
    return QQuickGraphsSurface::doPicking(position);
  }

  //  bool QQuickGraphsSurface::doRayPicking(QVector3D origin, QVector3D
  //      direction)
  bool doRayPicking(QVector3D origin, QVector3D direction) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall18 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall18>(taken[18]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsSurface::doRayPicking(origin, direction);
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsSurface::getSeriesMultiAxis(QAbstract3DSeries
  //      *series, QAbstract3DAxis::AxisOrientation orientation)
  QAbstract3DAxis *getSeriesMultiAxis(
      QAbstract3DSeries *series,
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall19 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall19>(taken[19]);
      void * given = call(this, series, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsSurface::getSeriesMultiAxis(series, orientation);
  }

  //  void QQuickGraphsSurface::createSliceView()
  void createSliceView() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall20 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::createSliceView();
  }

  //  void QQuickGraphsSurface::updateSliceItemLabel(const QString &label,
  //      QVector3D position)
  void updateSliceItemLabel(
      const QString &label,
      QVector3D position) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall21 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall21>(taken[21]);
      call(this, &label, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::updateSliceItemLabel(label, position);
  }

  //  void
  //      QQuickGraphsSurface::updateSelectionMode(QtGraphs3D::SelectionFla
  //      gs mode)
  void updateSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall22 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall22>(taken[22]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::updateSelectionMode(mode);
  }

  //  void QQuickGraphsSurface::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall23 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall23>(taken[23]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleAxisXChanged(axis);
  }

  //  void QQuickGraphsSurface::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall24 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall24>(taken[24]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleAxisYChanged(axis);
  }

  //  void QQuickGraphsSurface::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall25 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall25>(taken[25]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsSurface::handleAxisZChanged(axis);
  }

  //  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject
  //      *sender)
  void handleAxisTitleChangedBySender(QObject *sender) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall26 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall26>(taken[26]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject
  //      *sender)
  void handleAxisLabelsChangedBySender(QObject *sender) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall27 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall27>(taken[27]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelsChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
  //      *sender)
  void handleAxisSegmentCountChangedBySender(QObject *sender) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall28 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall28>(taken[28]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSegmentCountChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObjec
  //      t *sender)
  void handleAxisSubSegmentCountChangedBySender(QObject *sender) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall29 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall29>(taken[29]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
  //      *sender)
  void handleAxisLabelFormatChangedBySender(QObject *sender) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall30 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall30>(taken[30]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelFormatChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject
  //      *sender)
  void handleAxisReversedChangedBySender(QObject *sender) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall31 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall31>(taken[31]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisReversedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject
  //      *sender)
  void handleAxisFormatterDirtyBySender(QObject *sender) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall32 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall32>(taken[32]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisFormatterDirtyBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObj
  //      ect *sender)
  void handleAxisLabelAutoRotationChangedBySender(QObject *sender) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall33 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall33>(taken[33]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(QOb
  //      ject *sender)
  void handleAxisScaleLabelsByCountChangedBySender(
      QObject *sender) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall34 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall34>(taken[34]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
  //      *sender)
  void handleAxisLabelSizeChangedBySender(QObject *sender) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall35 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall35>(taken[35]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelSizeChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisTitleVisibilityChangedBySender(QObject *sender) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall36 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall36>(taken[36]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisLabelVisibilityChangedBySender(QObject *sender) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall37 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall37>(taken[37]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
  //      *sender)
  void handleAxisTitleFixedChangedBySender(QObject *sender) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall38 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall38>(taken[38]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleFixedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
  //      *sender)
  void handleAxisTitleOffsetChangedBySender(QObject *sender) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall39 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall39>(taken[39]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(sender);
  }

  //  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall40 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall40>(taken[40]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addSeriesInternal(series);
  }

  //  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries
  //      *series)
  void removeSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall41 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall41>(taken[41]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeSeriesInternal(series);
  }

  //  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
  void addAxis(QAbstract3DAxis *axis) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall42 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall42>(taken[42]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addAxis(axis);
  }

  //  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
  void releaseAxis(QAbstract3DAxis *axis) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall43 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall43>(taken[43]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseAxis(axis);
  }

  //  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode
  //      mode)
  void setRenderingMode(QtGraphs3D::RenderingMode mode) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall44 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall44>(taken[44]);
      call(this, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setRenderingMode(mode);
  }

  //  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
  QtGraphs3D::RenderingMode renderingMode() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall45 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall45>(taken[45]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::RenderingMode>(given);
    }
    return QQuickGraphsItem::renderingMode();
  }

  //  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::Transpare
  //      ncyTechnique technique)
  void setTransparencyTechnique(
      QtGraphs3D::TransparencyTechnique technique) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall46 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall46>(taken[46]);
      call(this, static_cast<int>(technique), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setTransparencyTechnique(technique);
  }

  //  QtGraphs3D::TransparencyTechnique
  //      QQuickGraphsItem::transparencyTechnique() const
  QtGraphs3D::TransparencyTechnique transparencyTechnique() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall47 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall47>(taken[47]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::TransparencyTechnique>(given);
    }
    return QQuickGraphsItem::transparencyTechnique();
  }

  //  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
  QtGraphs3D::SelectionFlags selectionMode() const override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall48 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall48>(taken[48]);
      int given = call(this, &handled);
      if (handled) return QFlags<QtGraphs3D::SelectionFlag>::fromInt(given);
    }
    return QQuickGraphsItem::selectionMode();
  }

  //  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void setShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall49 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall49>(taken[49]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setShadowQuality(quality);
  }

  //  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
  QtGraphs3D::ShadowQuality shadowQuality() const override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall50 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall50>(taken[50]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ShadowQuality>(given);
    }
    return QQuickGraphsItem::shadowQuality();
  }

  //  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
  QtGraphs3D::ElementType selectedElement() const override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall51 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall51>(taken[51]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ElementType>(given);
    }
    return QQuickGraphsItem::selectedElement();
  }

  //  void QQuickGraphsItem::setMsaaSamples(int samples)
  void setMsaaSamples(int samples) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall52 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall52>(taken[52]);
      call(this, samples, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setMsaaSamples(samples);
  }

  //  int QQuickGraphsItem::msaaSamples() const
  int msaaSamples() const override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall53 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall53>(taken[53]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::msaaSamples();
  }

  //  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall54 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall54>(taken[54]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::hasSeries(series);
  }

  //  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall55 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall55>(taken[55]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::addCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItems()
  void removeCustomItems() override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall56 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall56>(taken[56]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItems();
  }

  //  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall57 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall57>(taken[57]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall58 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall58>(taken[58]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItemAt(position);
  }

  //  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall59 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall59>(taken[59]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseCustomItem(item);
  }

  //  int QQuickGraphsItem::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall60 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall60>(taken[60]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[61]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall61 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall61>(taken[61]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::selectedAxis();
  }

  //  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall62 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall62>(taken[62]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall63 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall63>(taken[63]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCustom3DItem *>(given);
    }
    return QQuickGraphsItem::selectedCustomItem();
  }

  //  void QQuickGraphsItem::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall64 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall64>(taken[64]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickGraphsItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall65 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall65>(taken[65]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickGraphsItem::handleWindowChanged()
  void handleWindowChanged() override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall66 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall66>(taken[66]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleWindowChanged();
  }

  //  void QQuickGraphsItem::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall67 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall67>(taken[67]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::itemChange(change, value);
  }

  //  void QQuickGraphsItem::updateWindowParameters()
  void updateWindowParameters() override {
    if (taken[68]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall68 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall68>(taken[68]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateWindowParameters();
  }

  //  void QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::Selectio
  //      nFlags mode)
  void handleSelectionModeChange(QtGraphs3D::SelectionFlags mode) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall69 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall69>(taken[69]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSelectionModeChange(mode);
  }

  //  void
  //      QQuickGraphsItem::handleShadowQualityChange(QtGraphs3D::ShadowQua
  //      lity quality)
  void handleShadowQualityChange(
      QtGraphs3D::ShadowQuality quality) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall70 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall70>(taken[70]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleShadowQualityChange(quality);
  }

  //  void
  //      QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::Element
  //      Type type)
  void handleSelectedElementChange(QtGraphs3D::ElementType type) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall71 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall71>(taken[71]);
      call(this, static_cast<int>(type), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSelectedElementChange(type);
  }

  //  void QQuickGraphsItem::handleOptimizationHintChange(QtGraphs3D::Optim
  //      izationHint hint)
  void handleOptimizationHintChange(
      QtGraphs3D::OptimizationHint hint) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall72 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall72>(taken[72]);
      call(this, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleOptimizationHintChange(hint);
  }

  //  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall73 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall73>(taken[73]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::keyPressEvent(ev);
  }

  //  void QQuickGraphsItem::handleParentWidthChange()
  void handleParentWidthChange() override {
    if (taken[74]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall74 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall74>(taken[74]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentWidthChange();
  }

  //  void QQuickGraphsItem::handleParentHeightChange()
  void handleParentHeightChange() override {
    if (taken[75]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall75 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall75>(taken[75]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentHeightChange();
  }

  //  QVector3D
  //      QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis
  //      *axis, QVector3D labelPosition, int index)
  QVector3D calculateCategoryLabelPosition(
      QAbstract3DAxis *axis,
      QVector3D labelPosition,
      int index) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall76 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall76>(taken[76]);
      const QVector3D * given = call(this, axis, &labelPosition, index, &handled);
      if (handled && given) return *given;
    }
    return QQuickGraphsItem::calculateCategoryLabelPosition(axis, labelPosition, index);
  }

  //  float
  //      QQuickGraphsItem::calculateCategoryGridLinePosition(QAbstract3DAx
  //      is *axis, int index)
  float calculateCategoryGridLinePosition(
      QAbstract3DAxis *axis,
      int index) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall77 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall77>(taken[77]);
      float given = call(this, axis, index, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::calculateCategoryGridLinePosition(axis, index);
  }

  //  void QQuickGraphsItem::updateShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void updateShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall78 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall78>(taken[78]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateShadowQuality(quality);
  }

  //  void QQuickGraphsItem::updateAxisRange(float min, float max)
  void updateAxisRange(float min, float max) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall79 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall79>(taken[79]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateAxisRange(min, max);
  }

  //  void QQuickGraphsItem::updateAxisReversed(bool enable)
  void updateAxisReversed(bool enable) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall80 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall80>(taken[80]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateAxisReversed(enable);
  }

  //  void QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater
  //      *repeater, QColor axisLabelColor)
  void handleLabelCountChanged(
      QQuick3DRepeater *repeater,
      QColor axisLabelColor) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall81 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall81>(taken[81]);
      call(this, repeater, &axisLabelColor, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleLabelCountChanged(repeater, axisLabelColor);
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsItem::createDefaultAxis(QAbstract3DAxis::AxisOrienta
  //      tion orientation)
  QAbstract3DAxis *createDefaultAxis(
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall82 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall82>(taken[82]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::createDefaultAxis(orientation);
  }

  //  void QQuickGraphsItem::startRecordingRemovesAndInserts()
  void startRecordingRemovesAndInserts() override {
    if (taken[83]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall83 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall83>(taken[83]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::startRecordingRemovesAndInserts();
  }

  //  bool QQuick3DViewport::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[84]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall84 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall84>(taken[84]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DViewport::isTextureProvider();
  }

  //  QSGTextureProvider *QQuick3DViewport::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[85]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall85 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall85>(taken[85]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuick3DViewport::textureProvider();
  }

  //  void QQuick3DViewport::releaseResources()
  void releaseResources() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall86 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall86>(taken[86]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DViewport::releaseResources();
  }

  //  QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall87 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall87>(taken[87]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuick3DViewport::updatePaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[88]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall88 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall88>(taken[88]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[89]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall89 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall89>(taken[89]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[90]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall90 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall90>(taken[90]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[91]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall91 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall91>(taken[91]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[92]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall92 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall92>(taken[92]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall93 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall93>(taken[93]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall94 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall94>(taken[94]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall95 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall96 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall97 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall97>(taken[97]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall98 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall98>(taken[98]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall99 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall99>(taken[99]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall100 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall100>(taken[100]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall101 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[102]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall102 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall102>(taken[102]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall103 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall103>(taken[103]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall104 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall104>(taken[104]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall105 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall105>(taken[105]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall106 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall106>(taken[106]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall107 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall107>(taken[107]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall108 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall109 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall109>(taken[109]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall110 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall111 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall112 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall112>(taken[112]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[113]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall113 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall113>(taken[113]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall114 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall114>(taken[114]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall115 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall115>(taken[115]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall116 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall116>(taken[116]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall117 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall117>(taken[117]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall118 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall118>(taken[118]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQuickGraphsSurfaceCall119 call = reinterpret_cast<CuteQQuickGraphsSurfaceCall119>(taken[119]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickGraphsSurface10metaObjectEv(
    const QQuickGraphsSurface *self) {
  return self->metaObject();
}

//  QString QQuickGraphsSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickGraphsSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsSurface::tr(s, c, n));
}

//  QQuickGraphsSurface::QQuickGraphsSurface(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsSurface *ritual_ZN19QQuickGraphsSurfaceC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickGraphsSurface(parent);
}

//  QQuickGraphsSurface::~QQuickGraphsSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurfaceD1Ev(QQuickGraphsSurface *self) {
  delete self;
}

//  void QQuickGraphsSurface::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface8setAxisXEP12QValue3DAxis(
    QQuickGraphsSurface *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  QValue3DAxis *QQuickGraphsSurface::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK19QQuickGraphsSurface5axisXEv(
    const QQuickGraphsSurface *self) {
  return self->axisX();
}

//  void QQuickGraphsSurface::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface8setAxisYEP12QValue3DAxis(
    QQuickGraphsSurface *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  QValue3DAxis *QQuickGraphsSurface::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK19QQuickGraphsSurface5axisYEv(
    const QQuickGraphsSurface *self) {
  return self->axisY();
}

//  void QQuickGraphsSurface::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface8setAxisZEP12QValue3DAxis(
    QQuickGraphsSurface *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QValue3DAxis *QQuickGraphsSurface::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK19QQuickGraphsSurface5axisZEv(
    const QQuickGraphsSurface *self) {
  return self->axisZ();
}

//  void QQuickGraphsSurface::addSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface9addSeriesEP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    QSurface3DSeries *series) {
  self->addSeries(series);
}

//  void QQuickGraphsSurface::removeSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface12removeSeriesEP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    QSurface3DSeries *series) {
  self->removeSeries(series);
}

//  void QQuickGraphsSurface::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface14clearSelectionEv(
    QQuickGraphsSurface *self) {
  self->clearSelection();
}

//  void QQuickGraphsSurface::setFlipHorizontalGrid(bool flip)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface21setFlipHorizontalGridEb(
    QQuickGraphsSurface *self,
    bool flip) {
  self->setFlipHorizontalGrid(flip);
}

//  bool QQuickGraphsSurface::flipHorizontalGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface18flipHorizontalGridEv(
    const QQuickGraphsSurface *self) {
  return self->flipHorizontalGrid();
}

//  bool QQuickGraphsSurface::isFlatShadingSupported()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsSurface22isFlatShadingSupportedEv(
    QQuickGraphsSurface *self) {
  return self->isFlatShadingSupported();
}

//  QList<QSurface3DSeries *> QQuickGraphsSurface::surfaceSeriesList()
extern "C" Q_DECL_EXPORT
QList<QSurface3DSeries *> *ritual_ZN19QQuickGraphsSurface17surfaceSeriesListEv(
    QQuickGraphsSurface *self) {
  return new QList<QSurface3DSeries *>(self->surfaceSeriesList());
}

//  void QQuickGraphsSurface::updateSurfaceTexture(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface20updateSurfaceTextureEP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    QSurface3DSeries *series) {
  self->updateSurfaceTexture(series);
}

//  QPoint QQuickGraphsSurface::invalidSelectionPosition()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN19QQuickGraphsSurface24invalidSelectionPositionEv() {
  return new QPoint(QQuickGraphsSurface::invalidSelectionPosition());
}

//  void QQuickGraphsSurface::setSelectedPoint(QPoint position,
//      QSurface3DSeries *series, bool enterSlice)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface16setSelectedPointE6QPointP16QSurface3DSeriesb(
    QQuickGraphsSurface *self,
    const QPoint *position,
    QSurface3DSeries *series,
    bool enterSlice) {
  self->setSelectedPoint(*position, series, enterSlice);
}

//  QSurface3DSeries *QQuickGraphsSurface::selectedSeries() const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZNK19QQuickGraphsSurface14selectedSeriesEv(
    const QQuickGraphsSurface *self) {
  return self->selectedSeries();
}

//  void QQuickGraphsSurface::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsSurface *self,
    int mode) {
  self->setSelectionMode(QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsSurface::setDataDimensions(DataDimensions dimension)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface17setDataDimensionsE6QFlagsINS_13DataDimensionEE(
    QQuickGraphsSurface *self,
    int dimension) {
  self->setDataDimensions(
      QFlags<QQuickGraphsSurface::DataDimension>::fromInt(dimension));
}

//  DataDimensions QQuickGraphsSurface::dataDimensions()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickGraphsSurface14dataDimensionsEv(
    QQuickGraphsSurface *self) {
  return static_cast<int>(self->dataDimensions().toInt());
}

//  bool QQuickGraphsSurface::hasChangedSeriesList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface20hasChangedSeriesListEv(
    const QQuickGraphsSurface *self) {
  return self->hasChangedSeriesList();
}

//  bool QQuickGraphsSurface::isSeriesVisibilityDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface23isSeriesVisibilityDirtyEv(
    const QQuickGraphsSurface *self) {
  return self->isSeriesVisibilityDirty();
}

//  void QQuickGraphsSurface::setSeriesVisibilityDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface24setSeriesVisibilityDirtyEb(
    QQuickGraphsSurface *self,
    bool dirty) {
  self->setSeriesVisibilityDirty(dirty);
}

//  bool QQuickGraphsSurface::isDataDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface11isDataDirtyEv(
    const QQuickGraphsSurface *self) {
  return self->isDataDirty();
}

//  void QQuickGraphsSurface::setDataDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface12setDataDirtyEb(
    QQuickGraphsSurface *self,
    bool dirty) {
  self->setDataDirty(dirty);
}

//  bool QQuickGraphsSurface::isSeriesVisualsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface20isSeriesVisualsDirtyEv(
    const QQuickGraphsSurface *self) {
  return self->isSeriesVisualsDirty();
}

//  void QQuickGraphsSurface::setSeriesVisualsDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface21setSeriesVisualsDirtyEb(
    QQuickGraphsSurface *self,
    bool dirty) {
  self->setSeriesVisualsDirty(dirty);
}

//  bool QQuickGraphsSurface::isIndexDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface12isIndexDirtyEv(
    const QQuickGraphsSurface *self) {
  return self->isIndexDirty();
}

//  void QQuickGraphsSurface::setIndexDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface13setIndexDirtyEb(
    QQuickGraphsSurface *self,
    bool dirty) {
  self->setIndexDirty(dirty);
}

//  QList<QAbstract3DSeries *> QQuickGraphsSurface::changedSeriesList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DSeries *> *ritual_ZN19QQuickGraphsSurface17changedSeriesListEv(
    QQuickGraphsSurface *self) {
  return new QList<QAbstract3DSeries *>(self->changedSeriesList());
}

//  bool QQuickGraphsSurface::isSelectedPointChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface22isSelectedPointChangedEv(
    const QQuickGraphsSurface *self) {
  return self->isSelectedPointChanged();
}

//  void QQuickGraphsSurface::setSelectedPointChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface23setSelectedPointChangedEb(
    QQuickGraphsSurface *self,
    bool changed) {
  self->setSelectedPointChanged(changed);
}

//  bool QQuickGraphsSurface::isFlipHorizontalGridChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface27isFlipHorizontalGridChangedEv(
    const QQuickGraphsSurface *self) {
  return self->isFlipHorizontalGridChanged();
}

//  void QQuickGraphsSurface::setFlipHorizontalGridChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface28setFlipHorizontalGridChangedEb(
    QQuickGraphsSurface *self,
    bool changed) {
  self->setFlipHorizontalGridChanged(changed);
}

//  bool QQuickGraphsSurface::isSurfaceTextureChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface23isSurfaceTextureChangedEv(
    const QQuickGraphsSurface *self) {
  return self->isSurfaceTextureChanged();
}

//  void QQuickGraphsSurface::setSurfaceTextureChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface24setSurfaceTextureChangedEb(
    QQuickGraphsSurface *self,
    bool changed) {
  self->setSurfaceTextureChanged(changed);
}

//  bool QQuickGraphsSurface::isChangedTexturesEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface22isChangedTexturesEmptyEv(
    const QQuickGraphsSurface *self) {
  return self->isChangedTexturesEmpty();
}

//  bool QQuickGraphsSurface::hasSeriesToChangeTexture(QSurface3DSeries
//      *series) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsSurface24hasSeriesToChangeTextureEP16QSurface3DSeries(
    const QQuickGraphsSurface *self,
    QSurface3DSeries *series) {
  return self->hasSeriesToChangeTexture(series);
}

//  void QQuickGraphsSurface::handleAxisAutoAdjustRangeChangedInOrientation(Q
//      Abstract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsSurface *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsSurface::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsSurface *self,
    QObject *sender) {
  self->handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsSurface *self,
    QObject *sender) {
  self->handleSeriesVisibilityChangedBySender(sender);
}

//  void QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsSurface *self,
    bool visible,
    QObject *sender) {
  self->handleItemLabelVisibleChangedBySender(visible, sender);
}

//  void QQuickGraphsSurface::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface16adjustAxisRangesEv(
    QQuickGraphsSurface *self) {
  self->adjustAxisRanges();
}

//  void QQuickGraphsSurface::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->handleMultiAxisChanged(axis);
}

//  void QQuickGraphsSurface::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface25handleLightingModeChangedEv(
    QQuickGraphsSurface *self) {
  self->handleLightingModeChanged();
}

//  void QQuickGraphsSurface::renderSliceToImage(int index, int
//      requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface18renderSliceToImageEiiN10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsSurface *self,
    int index,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType) {
  self->renderSliceToImage(index, requestedIndex, sliceType);
}

//  void QQuickGraphsSurface::renderSliceToImage(int index, int
//      requestedIndex, QtGraphs3D::SliceCaptureType sliceType, const QUrl
//      &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface18renderSliceToImageEiiN10QtGraphs3D16SliceCaptureTypeERK4QUrl(
    QQuickGraphsSurface *self,
    int index,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType,
    const QUrl *filePath) {
  self->renderSliceToImage(index, requestedIndex, sliceType, *filePath);
}

//  void QQuickGraphsSurface::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface17componentCompleteEv(
    QQuickGraphsSurface *self) {
  self->componentComplete();
}

//  void QQuickGraphsSurface::synchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface9synchDataEv(QQuickGraphsSurface *self) {
  self->synchData();
}

//  void QQuickGraphsSurface::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface11updateGraphEv(
    QQuickGraphsSurface *self) {
  self->updateGraph();
}

//  void QQuickGraphsSurface::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface28calculateSceneScalingFactorsEv(
    QQuickGraphsSurface *self) {
  self->calculateSceneScalingFactors();
}

//  void QQuickGraphsSurface::toggleSliceGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface16toggleSliceGraphEv(
    QQuickGraphsSurface *self) {
  self->toggleSliceGraph();
}

//  void QQuickGraphsSurface::updateSingleHighlightColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface26updateSingleHighlightColorEv(
    QQuickGraphsSurface *self) {
  self->updateSingleHighlightColor();
}

//  void QQuickGraphsSurface::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface19updateLightStrengthEv(
    QQuickGraphsSurface *self) {
  self->updateLightStrength();
}

//  void QQuickGraphsSurface::handleThemeTypeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface21handleThemeTypeChangeEv(
    QQuickGraphsSurface *self) {
  self->handleThemeTypeChange();
}

//  bool QQuickGraphsSurface::doPicking(QPointF position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsSurface9doPickingE7QPointF(
    QQuickGraphsSurface *self,
    const QPointF *position) {
  return self->doPicking(*position);
}

//  bool QQuickGraphsSurface::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsSurface12doRayPickingE9QVector3DS0_(
    QQuickGraphsSurface *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  QAbstract3DAxis
//      *QQuickGraphsSurface::getSeriesMultiAxis(QAbstract3DSeries *series,
//      QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN19QQuickGraphsSurface18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsSurface *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->getSeriesMultiAxis(series, orientation);
}

//  void QQuickGraphsSurface::createSliceView()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface15createSliceViewEv(
    QQuickGraphsSurface *self) {
  self->createSliceView();
}

//  void QQuickGraphsSurface::updateSliceItemLabel(const QString &label,
//      QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface20updateSliceItemLabelERK7QString9QVector3D(
    QQuickGraphsSurface *self,
    const QString *label,
    const QVector3D *position) {
  self->updateSliceItemLabel(*label, *position);
}

//  void QQuickGraphsSurface::updateSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsSurface *self,
    int mode) {
  self->updateSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  QQuick3DViewport *QQuickGraphsSurface::createOffscreenSliceView(int
//      index, int requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN19QQuickGraphsSurface24createOffscreenSliceViewEiiN10QtGraphs3D16SliceCaptureTypeE(
    QQuickGraphsSurface *self,
    int index,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType) {
  return self->createOffscreenSliceView(index, requestedIndex, sliceType);
}

//  void QQuickGraphsSurface::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void QQuickGraphsSurface::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void QQuickGraphsSurface::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  void QQuickGraphsSurface::handleShadingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface20handleShadingChangedEv(
    QQuickGraphsSurface *self) {
  self->handleShadingChanged();
}

//  void QQuickGraphsSurface::handleWireframeColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface27handleWireframeColorChangedEv(
    QQuickGraphsSurface *self) {
  self->handleWireframeColorChanged();
}

//  void QQuickGraphsSurface::handleFlipHorizontalGridChanged(bool flip)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface31handleFlipHorizontalGridChangedEb(
    QQuickGraphsSurface *self,
    bool flip) {
  self->handleFlipHorizontalGridChanged(flip);
}

//  void QQuickGraphsSurface::handleArrayReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface16handleArrayResetEv(
    QQuickGraphsSurface *self) {
  self->handleArrayReset();
}

//  void QQuickGraphsSurface::handleRowsAdded(qsizetype startIndex, qsizetype
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface15handleRowsAddedExx(
    QQuickGraphsSurface *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsAdded(startIndex, count);
}

//  void QQuickGraphsSurface::handleRowsChanged(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface17handleRowsChangedExx(
    QQuickGraphsSurface *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsChanged(startIndex, count);
}

//  void QQuickGraphsSurface::handleRowsRemoved(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface17handleRowsRemovedExx(
    QQuickGraphsSurface *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsRemoved(startIndex, count);
}

//  void QQuickGraphsSurface::handleRowsInserted(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface18handleRowsInsertedExx(
    QQuickGraphsSurface *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleRowsInserted(startIndex, count);
}

//  void QQuickGraphsSurface::handleItemChanged(qsizetype rowIndex, qsizetype
//      columnIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface17handleItemChangedExx(
    QQuickGraphsSurface *self,
    qsizetype rowIndex,
    qsizetype columnIndex) {
  self->handleItemChanged(rowIndex, columnIndex);
}

//  void QQuickGraphsSurface::handleFlatShadingSupportedChange(bool
//      supported)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface32handleFlatShadingSupportedChangeEb(
    QQuickGraphsSurface *self,
    bool supported) {
  self->handleFlatShadingSupportedChange(supported);
}

//  QVector3D QQuickGraphsSurface::getNormalizedVertex(const QSurfaceDataItem
//      &data, bool polar, bool flipXZ, QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN19QQuickGraphsSurface19getNormalizedVertexERK16QSurfaceDataItembbP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    const QSurfaceDataItem *data,
    bool polar,
    bool flipXZ,
    QSurface3DSeries *series) {
  return new QVector3D(
      self->getNormalizedVertex(
          *data,
          polar,
          flipXZ,
          series));
}

//  void QQuickGraphsSurface::handleChangedSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface19handleChangedSeriesEv(
    QQuickGraphsSurface *self) {
  self->handleChangedSeries();
}

//  void QQuickGraphsSurface::updateSelectedPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface19updateSelectedPointEv(
    QQuickGraphsSurface *self) {
  self->updateSelectedPoint();
}

//  void QQuickGraphsSurface::addModel(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface8addModelEP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    QSurface3DSeries *series) {
  self->addModel(series);
}

//  void QQuickGraphsSurface::handleMeshTypeChanged(QAbstract3DSeries::Mesh
//      mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface21handleMeshTypeChangedEN17QAbstract3DSeries4MeshE(
    QQuickGraphsSurface *self,
    QAbstract3DSeries::Mesh mesh) {
  self->handleMeshTypeChanged(mesh);
}

//  void QQuickGraphsSurface::handlePointerChanged(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface20handlePointerChangedERK7QString(
    QQuickGraphsSurface *self,
    const QString *filename) {
  self->handlePointerChanged(*filename);
}

//  void QQuickGraphsSurface::changePointerMeshTypeForSeries(QAbstract3DSerie
//      s::Mesh mesh, QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface30changePointerMeshTypeForSeriesEN17QAbstract3DSeries4MeshEP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    QAbstract3DSeries::Mesh mesh,
    QSurface3DSeries *series) {
  self->changePointerMeshTypeForSeries(mesh, series);
}

//  void QQuickGraphsSurface::changePointerForSeries(const QString &filename,
//      QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface22changePointerForSeriesERK7QStringP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    const QString *filename,
    QSurface3DSeries *series) {
  self->changePointerForSeries(*filename, series);
}

//  void QQuickGraphsSurface::changeSlicePointerMeshTypeForSeries(QAbstract3D
//      Series::Mesh mesh, QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface35changeSlicePointerMeshTypeForSeriesEN17QAbstract3DSeries4MeshEP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    QAbstract3DSeries::Mesh mesh,
    QSurface3DSeries *series) {
  self->changeSlicePointerMeshTypeForSeries(mesh, series);
}

//  void QQuickGraphsSurface::changeSlicePointerForSeries(const QString
//      &filename, QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsSurface27changeSlicePointerForSeriesERK7QStringP16QSurface3DSeries(
    QQuickGraphsSurface *self,
    const QString *filename,
    QSurface3DSeries *series) {
  self->changeSlicePointerForSeries(*filename, series);
}

//  QString QQuickGraphsSurface::getMeshFileName(QAbstract3DSeries::Mesh
//      mesh, QSurface3DSeries *series) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickGraphsSurface15getMeshFileNameEN17QAbstract3DSeries4MeshEP16QSurface3DSeries(
    const QQuickGraphsSurface *self,
    QAbstract3DSeries::Mesh mesh,
    QSurface3DSeries *series) {
  return new QString(self->getMeshFileName(mesh, series));
}

//  bool QQuickGraphsSurface::intersectWithAABB(QVector3D boundMin, QVector3D
//      boundsMax, QVector3D origin, QVector3D dir)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsSurface17intersectWithAABBE9QVector3DS0_S0_S0_(
    QQuickGraphsSurface *self,
    const QVector3D *boundMin,
    const QVector3D *boundsMax,
    const QVector3D *origin,
    const QVector3D *dir) {
  return self->intersectWithAABB(*boundMin, *boundsMax, *origin, *dir);
}

//  a Python function taken by a CuteQQuickGraphsSurface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsSurface(
    QQuickGraphsSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsSurface *>(self)->take(key, call);
}

//  void QQuickGraphsSurface::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface14clearSelectionEv(
    QQuickGraphsSurface *self) {
  self->QQuickGraphsSurface::clearSelection();
}

//  void QQuickGraphsSurface::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsSurface *self,
    int mode) {
  self->QQuickGraphsSurface::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsSurface::handleAxisAutoAdjustRangeChangedInOrientation(Q
//      Abstract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsSurface *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->QQuickGraphsSurface::handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsSurface::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsSurface *self,
    QObject *sender) {
  self->QQuickGraphsSurface::handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsSurface *self,
    QObject *sender) {
  self->QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(sender);
}

//  void QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsSurface *self,
    bool visible,
    QObject *sender) {
  self->QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(
      visible,
      sender);
}

//  void QQuickGraphsSurface::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface16adjustAxisRangesEv(
    QQuickGraphsSurface *self) {
  self->QQuickGraphsSurface::adjustAxisRanges();
}

//  void QQuickGraphsSurface::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsSurface::handleMultiAxisChanged(axis);
}

//  void QQuickGraphsSurface::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface25handleLightingModeChangedEv(
    QQuickGraphsSurface *self) {
  self->QQuickGraphsSurface::handleLightingModeChanged();
}

//  void QQuickGraphsSurface::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface17componentCompleteEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::componentComplete();
}

//  void QQuickGraphsSurface::synchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface9synchDataEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::synchData();
}

//  void QQuickGraphsSurface::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface11updateGraphEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::updateGraph();
}

//  void QQuickGraphsSurface::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface28calculateSceneScalingFactorsEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::calculateSceneScalingFactors();
}

//  void QQuickGraphsSurface::toggleSliceGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface16toggleSliceGraphEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::toggleSliceGraph();
}

//  void QQuickGraphsSurface::updateSingleHighlightColor()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface26updateSingleHighlightColorEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::updateSingleHighlightColor();
}

//  void QQuickGraphsSurface::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface19updateLightStrengthEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::updateLightStrength();
}

//  void QQuickGraphsSurface::handleThemeTypeChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface21handleThemeTypeChangeEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::handleThemeTypeChange();
}

//  bool QQuickGraphsSurface::doPicking(QPointF position)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickGraphsSurface9doPickingE7QPointF(
    QQuickGraphsSurface *self,
    const QPointF *position) {
  return static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::doPicking(
      *position);
}

//  bool QQuickGraphsSurface::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickGraphsSurface12doRayPickingE9QVector3DS0_(
    QQuickGraphsSurface *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::doRayPicking(
      *origin,
      *direction);
}

//  QAbstract3DAxis
//      *QQuickGraphsSurface::getSeriesMultiAxis(QAbstract3DSeries *series,
//      QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN19QQuickGraphsSurface18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsSurface *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::getSeriesMultiAxis(
      series,
      orientation);
}

//  void QQuickGraphsSurface::createSliceView()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface15createSliceViewEv(
    QQuickGraphsSurface *self) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::createSliceView();
}

//  void QQuickGraphsSurface::updateSliceItemLabel(const QString &label,
//      QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface20updateSliceItemLabelERK7QString9QVector3D(
    QQuickGraphsSurface *self,
    const QString *label,
    const QVector3D *position) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::updateSliceItemLabel(
      *label,
      *position);
}

//  void QQuickGraphsSurface::updateSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsSurface *self,
    int mode) {
  static_cast<OwnQQuickGraphsSurface *>(self)->OwnQQuickGraphsSurface::updateSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsSurface::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsSurface::handleAxisXChanged(axis);
}

//  void QQuickGraphsSurface::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsSurface::handleAxisYChanged(axis);
}

//  void QQuickGraphsSurface::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsSurface18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsSurface *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsSurface::handleAxisZChanged(axis);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
