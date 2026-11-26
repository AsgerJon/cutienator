//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsscatter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphsscatter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGraphs/qscatter3dseries.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtGraphs/qabstract3dseries.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtGraphs/QScatter3DSeries>

//  Only a class built on QQuickGraphsScatter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGraphsScatter : QQuickGraphsScatter {
  using QQuickGraphsScatter::calculateSceneScalingFactors;
  using QQuickGraphsScatter::componentComplete;
  using QQuickGraphsScatter::doPicking;
  using QQuickGraphsScatter::doRayPicking;
  using QQuickGraphsScatter::updateShadowQuality;
  using QQuickGraphsScatter::updateLightStrength;
  using QQuickGraphsScatter::startRecordingRemovesAndInserts;
  using QQuickGraphsScatter::getSeriesMultiAxis;
};

//  A QQuickGraphsScatter that Python can take functions over in. Every QQuickGraphsScatter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickGraphsScatterCall0)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall1)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall2)(const void *, int, bool, int *);
typedef void (*CuteQQuickGraphsScatterCall3)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall4)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall5)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsScatterCall6)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall7)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsScatterCall8)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsScatterCall9)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsScatterCall10)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall11)(const void *, int *);
typedef bool (*CuteQQuickGraphsScatterCall12)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickGraphsScatterCall13)(const void *, const QVector3D *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsScatterCall14)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall15)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall16)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterCall17)(const void *, QAbstract3DSeries *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall18)(const void *, bool, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall19)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall20)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall21)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall22)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall23)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall24)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall25)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall26)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall27)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall28)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall29)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall30)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall31)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall32)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall33)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall34)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall35)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall36)(const void *, QObject *, int *);
typedef void (*CuteQQuickGraphsScatterCall37)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsScatterCall38)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteQQuickGraphsScatterCall39)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsScatterCall40)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQQuickGraphsScatterCall41)(const void *, int, int *);
typedef int (*CuteQQuickGraphsScatterCall42)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall43)(const void *, int, int *);
typedef int (*CuteQQuickGraphsScatterCall44)(const void *, int *);
typedef int (*CuteQQuickGraphsScatterCall45)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall46)(const void *, int, int *);
typedef int (*CuteQQuickGraphsScatterCall47)(const void *, int *);
typedef int (*CuteQQuickGraphsScatterCall48)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall49)(const void *, int, int *);
typedef int (*CuteQQuickGraphsScatterCall50)(const void *, int *);
typedef bool (*CuteQQuickGraphsScatterCall51)(const void *, QAbstract3DSeries *, int *);
typedef qsizetype (*CuteQQuickGraphsScatterCall52)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsScatterCall53)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall54)(const void *, QCustom3DItem *, int *);
typedef void (*CuteQQuickGraphsScatterCall55)(const void *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsScatterCall56)(const void *, QCustom3DItem *, int *);
typedef int (*CuteQQuickGraphsScatterCall57)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterCall58)(const void *, int *);
typedef qsizetype (*CuteQQuickGraphsScatterCall59)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterCall60)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall61)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickGraphsScatterCall62)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsScatterCall63)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterCall64)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall65)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsScatterCall66)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall67)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall68)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall69)(const void *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall71)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall72)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall73)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall74)(const void *, int *);
typedef const QVector3D * (*CuteQQuickGraphsScatterCall75)(const void *, QAbstract3DAxis *, const QVector3D *, int, int *);
typedef float (*CuteQQuickGraphsScatterCall76)(const void *, QAbstract3DAxis *, int, int *);
typedef void (*CuteQQuickGraphsScatterCall77)(const void *, const QString *, const QVector3D *, int *);
typedef void (*CuteQQuickGraphsScatterCall78)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall79)(const void *, float, float, int *);
typedef void (*CuteQQuickGraphsScatterCall80)(const void *, bool, int *);
typedef void (*CuteQQuickGraphsScatterCall81)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall82)(const void *, QQuick3DRepeater *, const QColor *, int *);
typedef void * (*CuteQQuickGraphsScatterCall83)(const void *, int, int *);
typedef bool (*CuteQQuickGraphsScatterCall84)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterCall85)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall86)(const void *, int *);
typedef void * (*CuteQQuickGraphsScatterCall87)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef const QRectF * (*CuteQQuickGraphsScatterCall88)(const void *, int *);
typedef const QRectF * (*CuteQQuickGraphsScatterCall89)(const void *, int *);
typedef bool (*CuteQQuickGraphsScatterCall90)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickGraphsScatterCall91)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsScatterCall92)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall93)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickGraphsScatterCall94)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickGraphsScatterCall95)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall96)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall97)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall98)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall99)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall100)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall101)(const void *, int *);
typedef void (*CuteQQuickGraphsScatterCall102)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsScatterCall103)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickGraphsScatterCall104)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall105)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall106)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall107)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsScatterCall108)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsScatterCall109)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsScatterCall110)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickGraphsScatterCall111)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickGraphsScatterCall112)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickGraphsScatterCall113)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsScatterCall114)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterCall115)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterCall116)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterCall117)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterCall118)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsScatterCall119)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsScatter : public QQuickGraphsScatter {
public:
  using QQuickGraphsScatter::QQuickGraphsScatter;
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
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16adjustAxisRangesEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22handleMultiAxisChangedEP15QAbstract3DAxis")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleLightingModeChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisXChangedEP15QAbstract3DAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisYChangedEP15QAbstract3DAxis")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18handleAxisZChangedEP15QAbstract3DAxis")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28calculateSceneScalingFactorsEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9doPickingE7QPointF")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem12doRayPickingE9QVector3DS0_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateLightStrengthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31startRecordingRemovesAndInsertsEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleItemLabelVisibleChangedBySenderEbP7QObject")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11updateGraphEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9synchDataEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleSeriesVisibilityChangedBySenderEP7QObject")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30handleAxisTitleChangedBySenderEP7QObject")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem31handleAxisLabelsChangedBySenderEP7QObject")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem37handleAxisSegmentCountChangedBySenderEP7QObject")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisSubSegmentCountChangedBySenderEP7QObject")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisLabelFormatChangedBySenderEP7QObject")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33handleAxisReversedChangedBySenderEP7QObject")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem32handleAxisFormatterDirtyBySenderEP7QObject")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem42handleAxisLabelAutoRotationChangedBySenderEP7QObject")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem43handleAxisScaleLabelsByCountChangedBySenderEP7QObject")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem34handleAxisLabelSizeChangedBySenderEP7QObject")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisTitleVisibilityChangedBySenderEP7QObject")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem40handleAxisLabelVisibilityChangedBySenderEP7QObject")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem35handleAxisTitleFixedChangedBySenderEP7QObject")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem36handleAxisTitleOffsetChangedBySenderEP7QObject")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17addSeriesInternalEP17QAbstract3DSeries")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20removeSeriesInternalEP17QAbstract3DSeries")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem7addAxisEP15QAbstract3DAxis")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem11releaseAxisEP15QAbstract3DAxis")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setRenderingModeEN10QtGraphs3D13RenderingModeE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13renderingModeEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem21transparencyTechniqueEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13selectionModeEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16setShadowQualityEN10QtGraphs3D13ShadowQualityE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem13shadowQualityEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem15selectedElementEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem14setMsaaSamplesEi")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem11msaaSamplesEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem9hasSeriesEP17QAbstract3DSeries")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem13addCustomItemEP13QCustom3DItem")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17removeCustomItemsEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16removeCustomItemEP13QCustom3DItem")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem18removeCustomItemAtE9QVector3D")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17releaseCustomItemEP13QCustom3DItem")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedLabelIndexEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem12selectedAxisEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem23selectedCustomItemIndexEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QQuickGraphsItem18selectedCustomItemEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19updateSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[62] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[63] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem19handleWindowChangedEv")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem22updateWindowParametersEv")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleSelectionModeChangeE6QFlagsIN10QtGraphs3D13SelectionFlagEE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem25handleShadowQualityChangeEN10QtGraphs3D13ShadowQualityE")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem27handleSelectedElementChangeEN10QtGraphs3D11ElementTypeE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem21handleThemeTypeChangeEv")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleParentWidthChangeEv")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem24handleParentHeightChangeEv")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem15createSliceViewEv")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem30calculateCategoryLabelPositionEP15QAbstract3DAxis9QVector3Di")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem33calculateCategoryGridLinePositionEP15QAbstract3DAxisi")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem20updateSliceItemLabelERK7QString9QVector3D")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem16toggleSliceGraphEv")) {
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
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem26updateSingleHighlightColorEv")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem23handleLabelCountChangedEP16QQuick3DRepeater6QColor")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQuickGraphsItem17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE")) {
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

  //  void QQuickGraphsScatter::clearSelection()
  void clearSelection() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall0 call = reinterpret_cast<CuteQQuickGraphsScatterCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::clearSelection();
  }

  //  void QQuickGraphsScatter::setSelectionMode(QtGraphs3D::SelectionFlags
  //      mode)
  void setSelectionMode(QtGraphs3D::SelectionFlags mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall1 call = reinterpret_cast<CuteQQuickGraphsScatterCall1>(taken[1]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::setSelectionMode(mode);
  }

  //  void QQuickGraphsScatter::handleAxisAutoAdjustRangeChangedInOrientati
  //      on(QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
  void handleAxisAutoAdjustRangeChangedInOrientation(
      QAbstract3DAxis::AxisOrientation orientation,
      bool autoAdjust) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall2 call = reinterpret_cast<CuteQQuickGraphsScatterCall2>(taken[2]);
      call(this, static_cast<int>(orientation), autoAdjust, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleAxisAutoAdjustRangeChangedInOrientation(orientation, autoAdjust);
  }

  //  void QQuickGraphsScatter::handleAxisRangeChangedBySender(QObject
  //      *sender)
  void handleAxisRangeChangedBySender(QObject *sender) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall3 call = reinterpret_cast<CuteQQuickGraphsScatterCall3>(taken[3]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleAxisRangeChangedBySender(sender);
  }

  //  void QQuickGraphsScatter::adjustAxisRanges()
  void adjustAxisRanges() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall4 call = reinterpret_cast<CuteQQuickGraphsScatterCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::adjustAxisRanges();
  }

  //  void QQuickGraphsScatter::handleMultiAxisChanged(QAbstract3DAxis
  //      *axis)
  void handleMultiAxisChanged(QAbstract3DAxis *axis) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall5 call = reinterpret_cast<CuteQQuickGraphsScatterCall5>(taken[5]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleMultiAxisChanged(axis);
  }

  //  void QQuickGraphsScatter::handleLightingModeChanged()
  void handleLightingModeChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall6 call = reinterpret_cast<CuteQQuickGraphsScatterCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleLightingModeChanged();
  }

  //  void QQuickGraphsScatter::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall7 call = reinterpret_cast<CuteQQuickGraphsScatterCall7>(taken[7]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleAxisXChanged(axis);
  }

  //  void QQuickGraphsScatter::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall8 call = reinterpret_cast<CuteQQuickGraphsScatterCall8>(taken[8]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleAxisYChanged(axis);
  }

  //  void QQuickGraphsScatter::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall9 call = reinterpret_cast<CuteQQuickGraphsScatterCall9>(taken[9]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleAxisZChanged(axis);
  }

  //  void QQuickGraphsScatter::calculateSceneScalingFactors()
  void calculateSceneScalingFactors() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall10 call = reinterpret_cast<CuteQQuickGraphsScatterCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::calculateSceneScalingFactors();
  }

  //  void QQuickGraphsScatter::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall11 call = reinterpret_cast<CuteQQuickGraphsScatterCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::componentComplete();
  }

  //  bool QQuickGraphsScatter::doPicking(QPointF position)
  bool doPicking(QPointF position) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall12 call = reinterpret_cast<CuteQQuickGraphsScatterCall12>(taken[12]);
      bool given = call(this, &position, &handled);
      if (handled) return given;
    }
    return QQuickGraphsScatter::doPicking(position);
  }

  //  bool QQuickGraphsScatter::doRayPicking(QVector3D origin, QVector3D
  //      direction)
  bool doRayPicking(QVector3D origin, QVector3D direction) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall13 call = reinterpret_cast<CuteQQuickGraphsScatterCall13>(taken[13]);
      bool given = call(this, &origin, &direction, &handled);
      if (handled) return given;
    }
    return QQuickGraphsScatter::doRayPicking(origin, direction);
  }

  //  void
  //      QQuickGraphsScatter::updateShadowQuality(QtGraphs3D::ShadowQualit
  //      y quality)
  void updateShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall14 call = reinterpret_cast<CuteQQuickGraphsScatterCall14>(taken[14]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::updateShadowQuality(quality);
  }

  //  void QQuickGraphsScatter::updateLightStrength()
  void updateLightStrength() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall15 call = reinterpret_cast<CuteQQuickGraphsScatterCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::updateLightStrength();
  }

  //  void QQuickGraphsScatter::startRecordingRemovesAndInserts()
  void startRecordingRemovesAndInserts() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall16 call = reinterpret_cast<CuteQQuickGraphsScatterCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::startRecordingRemovesAndInserts();
  }

  //  QAbstract3DAxis
  //      *QQuickGraphsScatter::getSeriesMultiAxis(QAbstract3DSeries
  //      *series, QAbstract3DAxis::AxisOrientation orientation)
  QAbstract3DAxis *getSeriesMultiAxis(
      QAbstract3DSeries *series,
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall17 call = reinterpret_cast<CuteQQuickGraphsScatterCall17>(taken[17]);
      void * given = call(this, series, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsScatter::getSeriesMultiAxis(series, orientation);
  }

  //  void QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(bool
  //      visible, QObject *sender)
  void handleItemLabelVisibleChangedBySender(
      bool visible,
      QObject *sender) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall18 call = reinterpret_cast<CuteQQuickGraphsScatterCall18>(taken[18]);
      call(this, visible, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(visible, sender);
  }

  //  void QQuickGraphsScatter::updateGraph()
  void updateGraph() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall19 call = reinterpret_cast<CuteQQuickGraphsScatterCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::updateGraph();
  }

  //  void QQuickGraphsScatter::synchData()
  void synchData() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall20 call = reinterpret_cast<CuteQQuickGraphsScatterCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::synchData();
  }

  //  void QQuickGraphsScatter::handleOptimizationHintChange(QtGraphs3D::Op
  //      timizationHint hint)
  void handleOptimizationHintChange(
      QtGraphs3D::OptimizationHint hint) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall21 call = reinterpret_cast<CuteQQuickGraphsScatterCall21>(taken[21]);
      call(this, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleOptimizationHintChange(hint);
  }

  //  void
  //      QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleSeriesVisibilityChangedBySender(QObject *sender) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall22 call = reinterpret_cast<CuteQQuickGraphsScatterCall22>(taken[22]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleChangedBySender(QObject
  //      *sender)
  void handleAxisTitleChangedBySender(QObject *sender) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall23 call = reinterpret_cast<CuteQQuickGraphsScatterCall23>(taken[23]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelsChangedBySender(QObject
  //      *sender)
  void handleAxisLabelsChangedBySender(QObject *sender) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall24 call = reinterpret_cast<CuteQQuickGraphsScatterCall24>(taken[24]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelsChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisSegmentCountChangedBySender(QObject
  //      *sender)
  void handleAxisSegmentCountChangedBySender(QObject *sender) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall25 call = reinterpret_cast<CuteQQuickGraphsScatterCall25>(taken[25]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSegmentCountChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(QObjec
  //      t *sender)
  void handleAxisSubSegmentCountChangedBySender(QObject *sender) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall26 call = reinterpret_cast<CuteQQuickGraphsScatterCall26>(taken[26]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisSubSegmentCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelFormatChangedBySender(QObject
  //      *sender)
  void handleAxisLabelFormatChangedBySender(QObject *sender) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall27 call = reinterpret_cast<CuteQQuickGraphsScatterCall27>(taken[27]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelFormatChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisReversedChangedBySender(QObject
  //      *sender)
  void handleAxisReversedChangedBySender(QObject *sender) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall28 call = reinterpret_cast<CuteQQuickGraphsScatterCall28>(taken[28]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisReversedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisFormatterDirtyBySender(QObject
  //      *sender)
  void handleAxisFormatterDirtyBySender(QObject *sender) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall29 call = reinterpret_cast<CuteQQuickGraphsScatterCall29>(taken[29]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisFormatterDirtyBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelAutoRotationChangedBySender(QObj
  //      ect *sender)
  void handleAxisLabelAutoRotationChangedBySender(QObject *sender) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall30 call = reinterpret_cast<CuteQQuickGraphsScatterCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall31 call = reinterpret_cast<CuteQQuickGraphsScatterCall31>(taken[31]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisScaleLabelsByCountChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisLabelSizeChangedBySender(QObject
  //      *sender)
  void handleAxisLabelSizeChangedBySender(QObject *sender) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall32 call = reinterpret_cast<CuteQQuickGraphsScatterCall32>(taken[32]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelSizeChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisTitleVisibilityChangedBySender(QObject *sender) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall33 call = reinterpret_cast<CuteQQuickGraphsScatterCall33>(taken[33]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleVisibilityChangedBySender(sender);
  }

  //  void
  //      QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(QObjec
  //      t *sender)
  void handleAxisLabelVisibilityChangedBySender(QObject *sender) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall34 call = reinterpret_cast<CuteQQuickGraphsScatterCall34>(taken[34]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisLabelVisibilityChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleFixedChangedBySender(QObject
  //      *sender)
  void handleAxisTitleFixedChangedBySender(QObject *sender) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall35 call = reinterpret_cast<CuteQQuickGraphsScatterCall35>(taken[35]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleFixedChangedBySender(sender);
  }

  //  void QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(QObject
  //      *sender)
  void handleAxisTitleOffsetChangedBySender(QObject *sender) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall36 call = reinterpret_cast<CuteQQuickGraphsScatterCall36>(taken[36]);
      call(this, sender, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleAxisTitleOffsetChangedBySender(sender);
  }

  //  void QQuickGraphsItem::addSeriesInternal(QAbstract3DSeries *series)
  void addSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall37 call = reinterpret_cast<CuteQQuickGraphsScatterCall37>(taken[37]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addSeriesInternal(series);
  }

  //  void QQuickGraphsItem::removeSeriesInternal(QAbstract3DSeries
  //      *series)
  void removeSeriesInternal(QAbstract3DSeries *series) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall38 call = reinterpret_cast<CuteQQuickGraphsScatterCall38>(taken[38]);
      call(this, series, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeSeriesInternal(series);
  }

  //  void QQuickGraphsItem::addAxis(QAbstract3DAxis *axis)
  void addAxis(QAbstract3DAxis *axis) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall39 call = reinterpret_cast<CuteQQuickGraphsScatterCall39>(taken[39]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::addAxis(axis);
  }

  //  void QQuickGraphsItem::releaseAxis(QAbstract3DAxis *axis)
  void releaseAxis(QAbstract3DAxis *axis) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall40 call = reinterpret_cast<CuteQQuickGraphsScatterCall40>(taken[40]);
      call(this, axis, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseAxis(axis);
  }

  //  void QQuickGraphsItem::setRenderingMode(QtGraphs3D::RenderingMode
  //      mode)
  void setRenderingMode(QtGraphs3D::RenderingMode mode) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall41 call = reinterpret_cast<CuteQQuickGraphsScatterCall41>(taken[41]);
      call(this, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setRenderingMode(mode);
  }

  //  QtGraphs3D::RenderingMode QQuickGraphsItem::renderingMode() const
  QtGraphs3D::RenderingMode renderingMode() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall42 call = reinterpret_cast<CuteQQuickGraphsScatterCall42>(taken[42]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::RenderingMode>(given);
    }
    return QQuickGraphsItem::renderingMode();
  }

  //  void QQuickGraphsItem::setTransparencyTechnique(QtGraphs3D::Transpare
  //      ncyTechnique technique)
  void setTransparencyTechnique(
      QtGraphs3D::TransparencyTechnique technique) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall43 call = reinterpret_cast<CuteQQuickGraphsScatterCall43>(taken[43]);
      call(this, static_cast<int>(technique), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setTransparencyTechnique(technique);
  }

  //  QtGraphs3D::TransparencyTechnique
  //      QQuickGraphsItem::transparencyTechnique() const
  QtGraphs3D::TransparencyTechnique transparencyTechnique() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall44 call = reinterpret_cast<CuteQQuickGraphsScatterCall44>(taken[44]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::TransparencyTechnique>(given);
    }
    return QQuickGraphsItem::transparencyTechnique();
  }

  //  QtGraphs3D::SelectionFlags QQuickGraphsItem::selectionMode() const
  QtGraphs3D::SelectionFlags selectionMode() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall45 call = reinterpret_cast<CuteQQuickGraphsScatterCall45>(taken[45]);
      int given = call(this, &handled);
      if (handled) return QFlags<QtGraphs3D::SelectionFlag>::fromInt(given);
    }
    return QQuickGraphsItem::selectionMode();
  }

  //  void QQuickGraphsItem::setShadowQuality(QtGraphs3D::ShadowQuality
  //      quality)
  void setShadowQuality(QtGraphs3D::ShadowQuality quality) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall46 call = reinterpret_cast<CuteQQuickGraphsScatterCall46>(taken[46]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setShadowQuality(quality);
  }

  //  QtGraphs3D::ShadowQuality QQuickGraphsItem::shadowQuality() const
  QtGraphs3D::ShadowQuality shadowQuality() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall47 call = reinterpret_cast<CuteQQuickGraphsScatterCall47>(taken[47]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ShadowQuality>(given);
    }
    return QQuickGraphsItem::shadowQuality();
  }

  //  QtGraphs3D::ElementType QQuickGraphsItem::selectedElement() const
  QtGraphs3D::ElementType selectedElement() const override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall48 call = reinterpret_cast<CuteQQuickGraphsScatterCall48>(taken[48]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtGraphs3D::ElementType>(given);
    }
    return QQuickGraphsItem::selectedElement();
  }

  //  void QQuickGraphsItem::setMsaaSamples(int samples)
  void setMsaaSamples(int samples) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall49 call = reinterpret_cast<CuteQQuickGraphsScatterCall49>(taken[49]);
      call(this, samples, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::setMsaaSamples(samples);
  }

  //  int QQuickGraphsItem::msaaSamples() const
  int msaaSamples() const override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall50 call = reinterpret_cast<CuteQQuickGraphsScatterCall50>(taken[50]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::msaaSamples();
  }

  //  bool QQuickGraphsItem::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall51 call = reinterpret_cast<CuteQQuickGraphsScatterCall51>(taken[51]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::hasSeries(series);
  }

  //  qsizetype QQuickGraphsItem::addCustomItem(QCustom3DItem *item)
  qsizetype addCustomItem(QCustom3DItem *item) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall52 call = reinterpret_cast<CuteQQuickGraphsScatterCall52>(taken[52]);
      qsizetype given = call(this, item, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::addCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItems()
  void removeCustomItems() override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall53 call = reinterpret_cast<CuteQQuickGraphsScatterCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItems();
  }

  //  void QQuickGraphsItem::removeCustomItem(QCustom3DItem *item)
  void removeCustomItem(QCustom3DItem *item) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall54 call = reinterpret_cast<CuteQQuickGraphsScatterCall54>(taken[54]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItem(item);
  }

  //  void QQuickGraphsItem::removeCustomItemAt(QVector3D position)
  void removeCustomItemAt(QVector3D position) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall55 call = reinterpret_cast<CuteQQuickGraphsScatterCall55>(taken[55]);
      call(this, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::removeCustomItemAt(position);
  }

  //  void QQuickGraphsItem::releaseCustomItem(QCustom3DItem *item)
  void releaseCustomItem(QCustom3DItem *item) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall56 call = reinterpret_cast<CuteQQuickGraphsScatterCall56>(taken[56]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::releaseCustomItem(item);
  }

  //  int QQuickGraphsItem::selectedLabelIndex() const
  int selectedLabelIndex() const override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall57 call = reinterpret_cast<CuteQQuickGraphsScatterCall57>(taken[57]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedLabelIndex();
  }

  //  QAbstract3DAxis *QQuickGraphsItem::selectedAxis() const
  QAbstract3DAxis *selectedAxis() const override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall58 call = reinterpret_cast<CuteQQuickGraphsScatterCall58>(taken[58]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::selectedAxis();
  }

  //  qsizetype QQuickGraphsItem::selectedCustomItemIndex() const
  qsizetype selectedCustomItemIndex() const override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall59 call = reinterpret_cast<CuteQQuickGraphsScatterCall59>(taken[59]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::selectedCustomItemIndex();
  }

  //  QCustom3DItem *QQuickGraphsItem::selectedCustomItem() const
  QCustom3DItem *selectedCustomItem() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall60 call = reinterpret_cast<CuteQQuickGraphsScatterCall60>(taken[60]);
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
    if (taken[61]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall61 call = reinterpret_cast<CuteQQuickGraphsScatterCall61>(taken[61]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickGraphsItem::updateSelectionMode(QtGraphs3D::SelectionFlags
  //      newMode)
  void updateSelectionMode(QtGraphs3D::SelectionFlags newMode) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall62 call = reinterpret_cast<CuteQQuickGraphsScatterCall62>(taken[62]);
      call(this, static_cast<int>(newMode.toInt()), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSelectionMode(newMode);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickGraphsItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall63 call = reinterpret_cast<CuteQQuickGraphsScatterCall63>(taken[63]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickGraphsItem::handleWindowChanged()
  void handleWindowChanged() override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall64 call = reinterpret_cast<CuteQQuickGraphsScatterCall64>(taken[64]);
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
    if (taken[65]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall65 call = reinterpret_cast<CuteQQuickGraphsScatterCall65>(taken[65]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::itemChange(change, value);
  }

  //  void QQuickGraphsItem::updateWindowParameters()
  void updateWindowParameters() override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall66 call = reinterpret_cast<CuteQQuickGraphsScatterCall66>(taken[66]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateWindowParameters();
  }

  //  void QQuickGraphsItem::handleSelectionModeChange(QtGraphs3D::Selectio
  //      nFlags mode)
  void handleSelectionModeChange(QtGraphs3D::SelectionFlags mode) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall67 call = reinterpret_cast<CuteQQuickGraphsScatterCall67>(taken[67]);
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
    if (taken[68]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall68 call = reinterpret_cast<CuteQQuickGraphsScatterCall68>(taken[68]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleShadowQualityChange(quality);
  }

  //  void
  //      QQuickGraphsItem::handleSelectedElementChange(QtGraphs3D::Element
  //      Type type)
  void handleSelectedElementChange(QtGraphs3D::ElementType type) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall69 call = reinterpret_cast<CuteQQuickGraphsScatterCall69>(taken[69]);
      call(this, static_cast<int>(type), &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleSelectedElementChange(type);
  }

  //  void QQuickGraphsItem::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall70 call = reinterpret_cast<CuteQQuickGraphsScatterCall70>(taken[70]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::keyPressEvent(ev);
  }

  //  void QQuickGraphsItem::handleThemeTypeChange()
  void handleThemeTypeChange() override {
    if (taken[71]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall71 call = reinterpret_cast<CuteQQuickGraphsScatterCall71>(taken[71]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleThemeTypeChange();
  }

  //  void QQuickGraphsItem::handleParentWidthChange()
  void handleParentWidthChange() override {
    if (taken[72]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall72 call = reinterpret_cast<CuteQQuickGraphsScatterCall72>(taken[72]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentWidthChange();
  }

  //  void QQuickGraphsItem::handleParentHeightChange()
  void handleParentHeightChange() override {
    if (taken[73]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall73 call = reinterpret_cast<CuteQQuickGraphsScatterCall73>(taken[73]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::handleParentHeightChange();
  }

  //  void QQuickGraphsItem::createSliceView()
  void createSliceView() override {
    if (taken[74]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall74 call = reinterpret_cast<CuteQQuickGraphsScatterCall74>(taken[74]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::createSliceView();
  }

  //  QVector3D
  //      QQuickGraphsItem::calculateCategoryLabelPosition(QAbstract3DAxis
  //      *axis, QVector3D labelPosition, int index)
  QVector3D calculateCategoryLabelPosition(
      QAbstract3DAxis *axis,
      QVector3D labelPosition,
      int index) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall75 call = reinterpret_cast<CuteQQuickGraphsScatterCall75>(taken[75]);
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
    if (taken[76]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall76 call = reinterpret_cast<CuteQQuickGraphsScatterCall76>(taken[76]);
      float given = call(this, axis, index, &handled);
      if (handled) return given;
    }
    return QQuickGraphsItem::calculateCategoryGridLinePosition(axis, index);
  }

  //  void QQuickGraphsItem::updateSliceItemLabel(const QString &label,
  //      QVector3D position)
  void updateSliceItemLabel(
      const QString &label,
      QVector3D position) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall77 call = reinterpret_cast<CuteQQuickGraphsScatterCall77>(taken[77]);
      call(this, &label, &position, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSliceItemLabel(label, position);
  }

  //  void QQuickGraphsItem::toggleSliceGraph()
  void toggleSliceGraph() override {
    if (taken[78]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall78 call = reinterpret_cast<CuteQQuickGraphsScatterCall78>(taken[78]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::toggleSliceGraph();
  }

  //  void QQuickGraphsItem::updateAxisRange(float min, float max)
  void updateAxisRange(float min, float max) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall79 call = reinterpret_cast<CuteQQuickGraphsScatterCall79>(taken[79]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateAxisRange(min, max);
  }

  //  void QQuickGraphsItem::updateAxisReversed(bool enable)
  void updateAxisReversed(bool enable) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall80 call = reinterpret_cast<CuteQQuickGraphsScatterCall80>(taken[80]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateAxisReversed(enable);
  }

  //  void QQuickGraphsItem::updateSingleHighlightColor()
  void updateSingleHighlightColor() override {
    if (taken[81]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall81 call = reinterpret_cast<CuteQQuickGraphsScatterCall81>(taken[81]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickGraphsItem::updateSingleHighlightColor();
  }

  //  void QQuickGraphsItem::handleLabelCountChanged(QQuick3DRepeater
  //      *repeater, QColor axisLabelColor)
  void handleLabelCountChanged(
      QQuick3DRepeater *repeater,
      QColor axisLabelColor) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall82 call = reinterpret_cast<CuteQQuickGraphsScatterCall82>(taken[82]);
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
    if (taken[83]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall83 call = reinterpret_cast<CuteQQuickGraphsScatterCall83>(taken[83]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return QQuickGraphsItem::createDefaultAxis(orientation);
  }

  //  bool QQuick3DViewport::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[84]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall84 call = reinterpret_cast<CuteQQuickGraphsScatterCall84>(taken[84]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DViewport::isTextureProvider();
  }

  //  QSGTextureProvider *QQuick3DViewport::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[85]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall85 call = reinterpret_cast<CuteQQuickGraphsScatterCall85>(taken[85]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuick3DViewport::textureProvider();
  }

  //  void QQuick3DViewport::releaseResources()
  void releaseResources() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall86 call = reinterpret_cast<CuteQQuickGraphsScatterCall86>(taken[86]);
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
      CuteQQuickGraphsScatterCall87 call = reinterpret_cast<CuteQQuickGraphsScatterCall87>(taken[87]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuick3DViewport::updatePaintNode(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[88]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall88 call = reinterpret_cast<CuteQQuickGraphsScatterCall88>(taken[88]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[89]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall89 call = reinterpret_cast<CuteQQuickGraphsScatterCall89>(taken[89]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[90]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall90 call = reinterpret_cast<CuteQQuickGraphsScatterCall90>(taken[90]);
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
      CuteQQuickGraphsScatterCall91 call = reinterpret_cast<CuteQQuickGraphsScatterCall91>(taken[91]);
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
      CuteQQuickGraphsScatterCall92 call = reinterpret_cast<CuteQQuickGraphsScatterCall92>(taken[92]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall93 call = reinterpret_cast<CuteQQuickGraphsScatterCall93>(taken[93]);
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
      CuteQQuickGraphsScatterCall94 call = reinterpret_cast<CuteQQuickGraphsScatterCall94>(taken[94]);
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
      CuteQQuickGraphsScatterCall95 call = reinterpret_cast<CuteQQuickGraphsScatterCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall96 call = reinterpret_cast<CuteQQuickGraphsScatterCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall97 call = reinterpret_cast<CuteQQuickGraphsScatterCall97>(taken[97]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall98 call = reinterpret_cast<CuteQQuickGraphsScatterCall98>(taken[98]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall99 call = reinterpret_cast<CuteQQuickGraphsScatterCall99>(taken[99]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall100 call = reinterpret_cast<CuteQQuickGraphsScatterCall100>(taken[100]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall101 call = reinterpret_cast<CuteQQuickGraphsScatterCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[102]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall102 call = reinterpret_cast<CuteQQuickGraphsScatterCall102>(taken[102]);
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
      CuteQQuickGraphsScatterCall103 call = reinterpret_cast<CuteQQuickGraphsScatterCall103>(taken[103]);
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
      CuteQQuickGraphsScatterCall104 call = reinterpret_cast<CuteQQuickGraphsScatterCall104>(taken[104]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall105 call = reinterpret_cast<CuteQQuickGraphsScatterCall105>(taken[105]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall106 call = reinterpret_cast<CuteQQuickGraphsScatterCall106>(taken[106]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall107 call = reinterpret_cast<CuteQQuickGraphsScatterCall107>(taken[107]);
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
      CuteQQuickGraphsScatterCall108 call = reinterpret_cast<CuteQQuickGraphsScatterCall108>(taken[108]);
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
      CuteQQuickGraphsScatterCall109 call = reinterpret_cast<CuteQQuickGraphsScatterCall109>(taken[109]);
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
      CuteQQuickGraphsScatterCall110 call = reinterpret_cast<CuteQQuickGraphsScatterCall110>(taken[110]);
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
      CuteQQuickGraphsScatterCall111 call = reinterpret_cast<CuteQQuickGraphsScatterCall111>(taken[111]);
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
      CuteQQuickGraphsScatterCall112 call = reinterpret_cast<CuteQQuickGraphsScatterCall112>(taken[112]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[113]) {
      int handled = 0;
      CuteQQuickGraphsScatterCall113 call = reinterpret_cast<CuteQQuickGraphsScatterCall113>(taken[113]);
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
      CuteQQuickGraphsScatterCall114 call = reinterpret_cast<CuteQQuickGraphsScatterCall114>(taken[114]);
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
      CuteQQuickGraphsScatterCall115 call = reinterpret_cast<CuteQQuickGraphsScatterCall115>(taken[115]);
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
      CuteQQuickGraphsScatterCall116 call = reinterpret_cast<CuteQQuickGraphsScatterCall116>(taken[116]);
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
      CuteQQuickGraphsScatterCall117 call = reinterpret_cast<CuteQQuickGraphsScatterCall117>(taken[117]);
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
      CuteQQuickGraphsScatterCall118 call = reinterpret_cast<CuteQQuickGraphsScatterCall118>(taken[118]);
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
      CuteQQuickGraphsScatterCall119 call = reinterpret_cast<CuteQQuickGraphsScatterCall119>(taken[119]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsScatter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickGraphsScatter10metaObjectEv(
    const QQuickGraphsScatter *self) {
  return self->metaObject();
}

//  void *QQuickGraphsScatter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickGraphsScatter11qt_metacastEPKc(
    QQuickGraphsScatter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphsScatter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickGraphsScatter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphsScatter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGraphsScatter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickGraphsScatter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsScatter::tr(s, c, n));
}

//  QQuickGraphsScatter::QQuickGraphsScatter(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsScatter *ritual_ZN19QQuickGraphsScatterC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickGraphsScatter(parent);
}

//  QQuickGraphsScatter::~QQuickGraphsScatter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatterD1Ev(QQuickGraphsScatter *self) {
  delete self;
}

//  void QQuickGraphsScatter::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter8setAxisXEP12QValue3DAxis(
    QQuickGraphsScatter *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  QValue3DAxis *QQuickGraphsScatter::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK19QQuickGraphsScatter5axisXEv(
    const QQuickGraphsScatter *self) {
  return self->axisX();
}

//  void QQuickGraphsScatter::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter8setAxisYEP12QValue3DAxis(
    QQuickGraphsScatter *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  QValue3DAxis *QQuickGraphsScatter::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK19QQuickGraphsScatter5axisYEv(
    const QQuickGraphsScatter *self) {
  return self->axisY();
}

//  void QQuickGraphsScatter::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter8setAxisZEP12QValue3DAxis(
    QQuickGraphsScatter *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QValue3DAxis *QQuickGraphsScatter::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK19QQuickGraphsScatter5axisZEv(
    const QQuickGraphsScatter *self) {
  return self->axisZ();
}

//  QQmlListProperty<QScatter3DSeries> QQuickGraphsScatter::seriesList()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QScatter3DSeries> *ritual_ZN19QQuickGraphsScatter10seriesListEv(
    QQuickGraphsScatter *self) {
  return new QQmlListProperty<QScatter3DSeries>(self->seriesList());
}

//  void
//      QQuickGraphsScatter::appendSeriesFunc(QQmlListProperty<QScatter3DSeri
//      es> *list, QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter16appendSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesEPS1_(
    QQmlListProperty<QScatter3DSeries> *list,
    QScatter3DSeries *series) {
  QQuickGraphsScatter::appendSeriesFunc(list, series);
}

//  qsizetype
//      QQuickGraphsScatter::countSeriesFunc(QQmlListProperty<QScatter3DSerie
//      s> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QQuickGraphsScatter15countSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesE(
    QQmlListProperty<QScatter3DSeries> *list) {
  return QQuickGraphsScatter::countSeriesFunc(list);
}

//  QScatter3DSeries
//      *QQuickGraphsScatter::atSeriesFunc(QQmlListProperty<QScatter3DSeries>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZN19QQuickGraphsScatter12atSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesEx(
    QQmlListProperty<QScatter3DSeries> *list,
    qsizetype index) {
  return QQuickGraphsScatter::atSeriesFunc(list, index);
}

//  void
//      QQuickGraphsScatter::clearSeriesFunc(QQmlListProperty<QScatter3DSerie
//      s> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter15clearSeriesFuncEP16QQmlListPropertyI16QScatter3DSeriesE(
    QQmlListProperty<QScatter3DSeries> *list) {
  QQuickGraphsScatter::clearSeriesFunc(list);
}

//  void QQuickGraphsScatter::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter14clearSelectionEv(
    QQuickGraphsScatter *self) {
  self->clearSelection();
}

//  void QQuickGraphsScatter::addSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter9addSeriesEP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    QScatter3DSeries *series) {
  self->addSeries(series);
}

//  void QQuickGraphsScatter::removeSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter12removeSeriesEP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    QScatter3DSeries *series) {
  self->removeSeries(series);
}

//  QList<QScatter3DSeries *> QQuickGraphsScatter::scatterSeriesList()
extern "C" Q_DECL_EXPORT
QList<QScatter3DSeries *> *ritual_ZN19QQuickGraphsScatter17scatterSeriesListEv(
    QQuickGraphsScatter *self) {
  return new QList<QScatter3DSeries *>(self->scatterSeriesList());
}

//  QScatter3DSeries *QQuickGraphsScatter::selectedSeries() const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZNK19QQuickGraphsScatter14selectedSeriesEv(
    const QQuickGraphsScatter *self) {
  return self->selectedSeries();
}

//  void QQuickGraphsScatter::setSelectedItem(qsizetype index,
//      QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter15setSelectedItemExP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    qsizetype index,
    QScatter3DSeries *series) {
  self->setSelectedItem(index, series);
}

//  qsizetype QQuickGraphsScatter::invalidSelectionIndex()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QQuickGraphsScatter21invalidSelectionIndexEv() {
  return QQuickGraphsScatter::invalidSelectionIndex();
}

//  void QQuickGraphsScatter::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsScatter *self,
    int mode) {
  self->setSelectionMode(QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  bool QQuickGraphsScatter::hasSelectedItemChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsScatter22hasSelectedItemChangedEv(
    const QQuickGraphsScatter *self) {
  return self->hasSelectedItemChanged();
}

//  void QQuickGraphsScatter::setSelectedItemChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter22setSelectedItemChangedEb(
    QQuickGraphsScatter *self,
    bool changed) {
  self->setSelectedItemChanged(changed);
}

//  bool QQuickGraphsScatter::hasItemChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsScatter14hasItemChangedEv(
    const QQuickGraphsScatter *self) {
  return self->hasItemChanged();
}

//  void QQuickGraphsScatter::setItemChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter14setItemChangedEb(
    QQuickGraphsScatter *self,
    bool changed) {
  self->setItemChanged(changed);
}

//  void QQuickGraphsScatter::handleAxisAutoAdjustRangeChangedInOrientation(Q
//      Abstract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsScatter *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsScatter::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsScatter *self,
    QObject *sender) {
  self->handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsScatter::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter16adjustAxisRangesEv(
    QQuickGraphsScatter *self) {
  self->adjustAxisRanges();
}

//  void QQuickGraphsScatter::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->handleMultiAxisChanged(axis);
}

//  bool QQuickGraphsScatter::hasChangedSeriesList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsScatter20hasChangedSeriesListEv(
    const QQuickGraphsScatter *self) {
  return self->hasChangedSeriesList();
}

//  bool QQuickGraphsScatter::isSeriesVisualsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsScatter20isSeriesVisualsDirtyEv(
    const QQuickGraphsScatter *self) {
  return self->isSeriesVisualsDirty();
}

//  void QQuickGraphsScatter::setSeriesVisualsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter21setSeriesVisualsDirtyEv(
    QQuickGraphsScatter *self) {
  self->setSeriesVisualsDirty();
}

//  bool QQuickGraphsScatter::isDataDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickGraphsScatter11isDataDirtyEv(
    const QQuickGraphsScatter *self) {
  return self->isDataDirty();
}

//  void QQuickGraphsScatter::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter25handleLightingModeChangedEv(
    QQuickGraphsScatter *self) {
  self->handleLightingModeChanged();
}

//  void QQuickGraphsScatter::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void QQuickGraphsScatter::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void QQuickGraphsScatter::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  void QQuickGraphsScatter::handleSeriesMeshChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter23handleSeriesMeshChangedEv(
    QQuickGraphsScatter *self) {
  self->handleSeriesMeshChanged();
}

//  void QQuickGraphsScatter::handleMeshSmoothChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter23handleMeshSmoothChangedEb(
    QQuickGraphsScatter *self,
    bool enable) {
  self->handleMeshSmoothChanged(enable);
}

//  void QQuickGraphsScatter::handleArrayReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter16handleArrayResetEv(
    QQuickGraphsScatter *self) {
  self->handleArrayReset();
}

//  void QQuickGraphsScatter::handleItemsAdded(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter16handleItemsAddedExx(
    QQuickGraphsScatter *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleItemsAdded(startIndex, count);
}

//  void QQuickGraphsScatter::handleItemsChanged(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter18handleItemsChangedExx(
    QQuickGraphsScatter *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleItemsChanged(startIndex, count);
}

//  void QQuickGraphsScatter::handleItemsRemoved(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter18handleItemsRemovedExx(
    QQuickGraphsScatter *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleItemsRemoved(startIndex, count);
}

//  void QQuickGraphsScatter::handleItemsInserted(qsizetype startIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19handleItemsInsertedExx(
    QQuickGraphsScatter *self,
    qsizetype startIndex,
    qsizetype count) {
  self->handleItemsInserted(startIndex, count);
}

//  void QQuickGraphsScatter::axisXChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter12axisXChangedEP12QValue3DAxis(
    QQuickGraphsScatter *self,
    QValue3DAxis *axis) {
  self->axisXChanged(axis);
}

//  void QQuickGraphsScatter::axisYChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter12axisYChangedEP12QValue3DAxis(
    QQuickGraphsScatter *self,
    QValue3DAxis *axis) {
  self->axisYChanged(axis);
}

//  void QQuickGraphsScatter::axisZChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter12axisZChangedEP12QValue3DAxis(
    QQuickGraphsScatter *self,
    QValue3DAxis *axis) {
  self->axisZChanged(axis);
}

//  void QQuickGraphsScatter::selectedSeriesChanged(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter21selectedSeriesChangedEP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    QScatter3DSeries *series) {
  self->selectedSeriesChanged(series);
}

//  void QQuickGraphsScatter::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter28calculateSceneScalingFactorsEv(
    QQuickGraphsScatter *self) {
  self->calculateSceneScalingFactors();
}

//  void QQuickGraphsScatter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter17componentCompleteEv(
    QQuickGraphsScatter *self) {
  self->componentComplete();
}

//  bool QQuickGraphsScatter::doPicking(QPointF position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsScatter9doPickingE7QPointF(
    QQuickGraphsScatter *self,
    const QPointF *position) {
  return self->doPicking(*position);
}

//  bool QQuickGraphsScatter::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsScatter12doRayPickingE9QVector3DS0_(
    QQuickGraphsScatter *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->doRayPicking(*origin, *direction);
}

//  void QQuickGraphsScatter::updateShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19updateShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsScatter *self,
    QtGraphs3D::ShadowQuality quality) {
  self->updateShadowQuality(quality);
}

//  void QQuickGraphsScatter::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19updateLightStrengthEv(
    QQuickGraphsScatter *self) {
  self->updateLightStrength();
}

//  void QQuickGraphsScatter::startRecordingRemovesAndInserts()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter31startRecordingRemovesAndInsertsEv(
    QQuickGraphsScatter *self) {
  self->startRecordingRemovesAndInserts();
}

//  QAbstract3DAxis
//      *QQuickGraphsScatter::getSeriesMultiAxis(QAbstract3DSeries *series,
//      QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN19QQuickGraphsScatter18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsScatter *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->getSeriesMultiAxis(series, orientation);
}

//  void QQuickGraphsScatter::connectSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter13connectSeriesEP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    QScatter3DSeries *series) {
  self->connectSeries(series);
}

//  void QQuickGraphsScatter::disconnectSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter16disconnectSeriesEP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    QScatter3DSeries *series) {
  self->disconnectSeries(series);
}

//  qsizetype QQuickGraphsScatter::getItemIndex(QQuick3DModel *item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QQuickGraphsScatter12getItemIndexEP13QQuick3DModel(
    QQuickGraphsScatter *self,
    QQuick3DModel *item) {
  return self->getItemIndex(item);
}

//  QVector3D QQuickGraphsScatter::selectedItemPosition()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN19QQuickGraphsScatter20selectedItemPositionEv(
    QQuickGraphsScatter *self) {
  return new QVector3D(self->selectedItemPosition());
}

//  void QQuickGraphsScatter::updateMaterialReference(ScatterModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter23updateMaterialReferenceEPNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *model) {
  self->updateMaterialReference(model);
}

//  void QQuickGraphsScatter::updateInstancedMaterialProperties(ScatterModel
//      *graphModel, const bool isHighlight, QQuick3DTexture *seriesTexture,
//      QQuick3DTexture *highlightTexture, const bool transparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter33updateInstancedMaterialPropertiesEPNS_12ScatterModelEbP15QQuick3DTextureS3_b(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *graphModel,
    bool isHighlight,
    QQuick3DTexture *seriesTexture,
    QQuick3DTexture *highlightTexture,
    bool transparency) {
  self->updateInstancedMaterialProperties(
      graphModel,
      isHighlight,
      seriesTexture,
      highlightTexture,
      transparency);
}

//  void QQuickGraphsScatter::updateItemMaterial(QQuick3DModel *item, bool
//      useGradient, bool rangeGradient, bool usePoint, const QString
//      &materialName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter18updateItemMaterialEP13QQuick3DModelbbbRK7QString(
    QQuickGraphsScatter *self,
    QQuick3DModel *item,
    bool useGradient,
    bool rangeGradient,
    bool usePoint,
    const QString *materialName) {
  self->updateItemMaterial(
      item,
      useGradient,
      rangeGradient,
      usePoint,
      *materialName);
}

//  void QQuickGraphsScatter::updateMaterialProperties(QQuick3DModel *item,
//      QQuick3DTexture *texture, QColor color, const bool transparency,
//      const bool shaded)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter24updateMaterialPropertiesEP13QQuick3DModelP15QQuick3DTexture6QColorbb(
    QQuickGraphsScatter *self,
    QQuick3DModel *item,
    QQuick3DTexture *texture,
    const QColor *color,
    bool transparency,
    bool shaded) {
  self->updateMaterialProperties(
      item,
      texture,
      *color,
      transparency,
      shaded);
}

//  QQuick3DTexture *QQuickGraphsScatter::createTexture()
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZN19QQuickGraphsScatter13createTextureEv(
    QQuickGraphsScatter *self) {
  return self->createTexture();
}

//  QQuick3DNode *QQuickGraphsScatter::createSeriesRoot()
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN19QQuickGraphsScatter16createSeriesRootEv(
    QQuickGraphsScatter *self) {
  return self->createSeriesRoot();
}

//  QQuick3DModel *QQuickGraphsScatter::createDataItem(QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZN19QQuickGraphsScatter14createDataItemEP17QAbstract3DSeries(
    QQuickGraphsScatter *self,
    QAbstract3DSeries *series) {
  return self->createDataItem(series);
}

//  void QQuickGraphsScatter::removeDataItems(ScatterModel *graphModel,
//      QtGraphs3D::OptimizationHint optimizationHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter15removeDataItemsEPNS_12ScatterModelEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *graphModel,
    QtGraphs3D::OptimizationHint optimizationHint) {
  self->removeDataItems(graphModel, optimizationHint);
}

//  void QQuickGraphsScatter::fixMeshFileName(QString &fileName,
//      QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter15fixMeshFileNameER7QStringP17QAbstract3DSeries(
    QQuickGraphsScatter *self,
    QString *fileName,
    QAbstract3DSeries *series) {
  self->fixMeshFileName(*fileName, series);
}

//  QString QQuickGraphsScatter::getMeshFileName(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickGraphsScatter15getMeshFileNameEP17QAbstract3DSeries(
    QQuickGraphsScatter *self,
    QAbstract3DSeries *series) {
  return new QString(self->getMeshFileName(series));
}

//  void QQuickGraphsScatter::deleteDataItem(QQuick3DModel *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter14deleteDataItemEP13QQuick3DModel(
    QQuickGraphsScatter *self,
    QQuick3DModel *item) {
  self->deleteDataItem(item);
}

//  void QQuickGraphsScatter::removeDataItems(QList<QQuick3DModel *> &items,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter15removeDataItemsER5QListIP13QQuick3DModelEx(
    QQuickGraphsScatter *self,
    QList<QQuick3DModel *> *items,
    qsizetype count) {
  self->removeDataItems(*items, count);
}

//  void QQuickGraphsScatter::recreateDataItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter17recreateDataItemsEv(
    QQuickGraphsScatter *self) {
  self->recreateDataItems();
}

//  void QQuickGraphsScatter::recreateDataItems(const QList<ScatterModel *>
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter17recreateDataItemsERK5QListIPNS_12ScatterModelEE(
    QQuickGraphsScatter *self,
    const QList<QQuickGraphsScatter::ScatterModel *> *a0) {
  self->recreateDataItems(*a0);
}

//  void QQuickGraphsScatter::addPointsToScatterModel(ScatterModel
//      *graphModel, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter23addPointsToScatterModelEPNS_12ScatterModelEx(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *graphModel,
    qsizetype count) {
  self->addPointsToScatterModel(graphModel, count);
}

//  qsizetype QQuickGraphsScatter::sizeDifference(qsizetype size1, qsizetype
//      size2)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QQuickGraphsScatter14sizeDifferenceExx(
    QQuickGraphsScatter *self,
    qsizetype size1,
    qsizetype size2) {
  return self->sizeDifference(size1, size2);
}

//  void QQuickGraphsScatter::handleSeriesChanged(QList<QAbstract3DSeries *>
//      changedSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19handleSeriesChangedE5QListIP17QAbstract3DSeriesE(
    QQuickGraphsScatter *self,
    const QList<QAbstract3DSeries *> *changedSeries) {
  self->handleSeriesChanged(*changedSeries);
}

//  bool QQuickGraphsScatter::selectedItemInSeries(const QScatter3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsScatter20selectedItemInSeriesEPK16QScatter3DSeries(
    QQuickGraphsScatter *self,
    const QScatter3DSeries *series) {
  return self->selectedItemInSeries(series);
}

//  bool QQuickGraphsScatter::isDotPositionInAxisRange(QVector3D dotPos,
//      QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsScatter24isDotPositionInAxisRangeE9QVector3DP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    const QVector3D *dotPos,
    QScatter3DSeries *series) {
  return self->isDotPositionInAxisRange(*dotPos, series);
}

//  float QQuickGraphsScatter::calculatePointScaleSize()
extern "C" Q_DECL_EXPORT
float ritual_ZN19QQuickGraphsScatter23calculatePointScaleSizeEv(
    QQuickGraphsScatter *self) {
  return self->calculatePointScaleSize();
}

//  void QQuickGraphsScatter::updatePointScaleSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter20updatePointScaleSizeEv(
    QQuickGraphsScatter *self) {
  self->updatePointScaleSize();
}

//  void QQuickGraphsScatter::calculatePolarXZ(const float posX, const float
//      posZ, float &x, float &z) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQuickGraphsScatter16calculatePolarXZEffRfS0_(
    const QQuickGraphsScatter *self,
    float posX,
    float posZ,
    float *x,
    float *z) {
  self->calculatePolarXZ(posX, posZ, *x, *z);
}

//  void QQuickGraphsScatter::updateSpline(ScatterModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter12updateSplineEPNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *model) {
  self->updateSpline(model);
}

//  void QQuickGraphsScatter::createSplineModel(ScatterModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter17createSplineModelEPNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *model) {
  self->createSplineModel(model);
}

//  void QQuickGraphsScatter::handleSplineChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19handleSplineChangedEv(
    QQuickGraphsScatter *self) {
  self->handleSplineChanged();
}

//  void QQuickGraphsScatter::generatePointsForScatterModel(ScatterModel
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter29generatePointsForScatterModelEPNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *series) {
  self->generatePointsForScatterModel(series);
}

//  void QQuickGraphsScatter::updateScatterGraphItemPositions(ScatterModel
//      *graphModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter31updateScatterGraphItemPositionsEPNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *graphModel) {
  self->updateScatterGraphItemPositions(graphModel);
}

//  void QQuickGraphsScatter::updateScatterGraphItemVisuals(ScatterModel
//      *graphModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter29updateScatterGraphItemVisualsEPNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    QQuickGraphsScatter::ScatterModel *graphModel) {
  self->updateScatterGraphItemVisuals(graphModel);
}

//  QQuick3DModel *QQuickGraphsScatter::selected() const
extern "C" Q_DECL_EXPORT
QQuick3DModel *ritual_ZNK19QQuickGraphsScatter8selectedEv(
    const QQuickGraphsScatter *self) {
  return self->selected();
}

//  void QQuickGraphsScatter::setSelected(QQuick3DModel *newSelected)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter11setSelectedEP13QQuick3DModel(
    QQuickGraphsScatter *self,
    QQuick3DModel *newSelected) {
  self->setSelected(newSelected);
}

//  void QQuickGraphsScatter::setSelected(QQuick3DModel *root, qsizetype
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter11setSelectedEP13QQuick3DModelx(
    QQuickGraphsScatter *self,
    QQuick3DModel *root,
    qsizetype index) {
  self->setSelected(root, index);
}

//  void QQuickGraphsScatter::clearSelectionModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19clearSelectionModelEv(
    QQuickGraphsScatter *self) {
  self->clearSelectionModel();
}

//  void QQuickGraphsScatter::clearAllSelectionInstanced()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter26clearAllSelectionInstancedEv(
    QQuickGraphsScatter *self) {
  self->clearAllSelectionInstanced();
}

//  void QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsScatter *self,
    bool visible,
    QObject *sender) {
  self->handleItemLabelVisibleChangedBySender(visible, sender);
}

//  void
//      QQuickGraphsScatter::optimizationChanged(QtGraphs3D::OptimizationHint
//      toOptimization)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter19optimizationChangedEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsScatter *self,
    QtGraphs3D::OptimizationHint toOptimization) {
  self->optimizationChanged(toOptimization);
}

//  void QQuickGraphsScatter::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter11updateGraphEv(
    QQuickGraphsScatter *self) {
  self->updateGraph();
}

//  void QQuickGraphsScatter::synchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter9synchDataEv(QQuickGraphsScatter *self) {
  self->synchData();
}

//  void QQuickGraphsScatter::handleOptimizationHintChange(QtGraphs3D::Optimi
//      zationHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsScatter *self,
    QtGraphs3D::OptimizationHint hint) {
  self->handleOptimizationHintChange(hint);
}

//  void QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsScatter *self,
    QObject *sender) {
  self->handleSeriesVisibilityChangedBySender(sender);
}

//  bool QQuickGraphsScatter::selectedItemInRange(const ScatterModel
//      *graphModel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickGraphsScatter19selectedItemInRangeEPKNS_12ScatterModelE(
    QQuickGraphsScatter *self,
    const QQuickGraphsScatter::ScatterModel *graphModel) {
  return self->selectedItemInRange(graphModel);
}

//  ScatterModel *QQuickGraphsScatter::findGraphModel(QScatter3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
QQuickGraphsScatter::ScatterModel *ritual_ZN19QQuickGraphsScatter14findGraphModelEP16QScatter3DSeries(
    QQuickGraphsScatter *self,
    QScatter3DSeries *series) {
  return self->findGraphModel(series);
}

//  void QQuickGraphsScatter::cameraRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickGraphsScatter21cameraRotationChangedEv(
    QQuickGraphsScatter *self) {
  self->cameraRotationChanged();
}

//  a Python function taken by a CuteQQuickGraphsScatter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsScatter(
    QQuickGraphsScatter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsScatter *>(self)->take(key, call);
}

//  void QQuickGraphsScatter::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter14clearSelectionEv(
    QQuickGraphsScatter *self) {
  self->QQuickGraphsScatter::clearSelection();
}

//  void QQuickGraphsScatter::setSelectionMode(QtGraphs3D::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter16setSelectionModeE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    QQuickGraphsScatter *self,
    int mode) {
  self->QQuickGraphsScatter::setSelectionMode(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(mode));
}

//  void QQuickGraphsScatter::handleAxisAutoAdjustRangeChangedInOrientation(Q
//      Abstract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    QQuickGraphsScatter *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->QQuickGraphsScatter::handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void QQuickGraphsScatter::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter30handleAxisRangeChangedBySenderEP7QObject(
    QQuickGraphsScatter *self,
    QObject *sender) {
  self->QQuickGraphsScatter::handleAxisRangeChangedBySender(sender);
}

//  void QQuickGraphsScatter::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter16adjustAxisRangesEv(
    QQuickGraphsScatter *self) {
  self->QQuickGraphsScatter::adjustAxisRanges();
}

//  void QQuickGraphsScatter::handleMultiAxisChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter22handleMultiAxisChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsScatter::handleMultiAxisChanged(axis);
}

//  void QQuickGraphsScatter::handleLightingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter25handleLightingModeChangedEv(
    QQuickGraphsScatter *self) {
  self->QQuickGraphsScatter::handleLightingModeChanged();
}

//  void QQuickGraphsScatter::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter18handleAxisXChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsScatter::handleAxisXChanged(axis);
}

//  void QQuickGraphsScatter::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter18handleAxisYChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsScatter::handleAxisYChanged(axis);
}

//  void QQuickGraphsScatter::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter18handleAxisZChangedEP15QAbstract3DAxis(
    QQuickGraphsScatter *self,
    QAbstract3DAxis *axis) {
  self->QQuickGraphsScatter::handleAxisZChanged(axis);
}

//  void QQuickGraphsScatter::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter28calculateSceneScalingFactorsEv(
    QQuickGraphsScatter *self) {
  static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::calculateSceneScalingFactors();
}

//  void QQuickGraphsScatter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter17componentCompleteEv(
    QQuickGraphsScatter *self) {
  static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::componentComplete();
}

//  bool QQuickGraphsScatter::doPicking(QPointF position)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickGraphsScatter9doPickingE7QPointF(
    QQuickGraphsScatter *self,
    const QPointF *position) {
  return static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::doPicking(
      *position);
}

//  bool QQuickGraphsScatter::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickGraphsScatter12doRayPickingE9QVector3DS0_(
    QQuickGraphsScatter *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::doRayPicking(
      *origin,
      *direction);
}

//  void QQuickGraphsScatter::updateShadowQuality(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter19updateShadowQualityEN10QtGraphs3D13ShadowQualityE(
    QQuickGraphsScatter *self,
    QtGraphs3D::ShadowQuality quality) {
  static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::updateShadowQuality(
      quality);
}

//  void QQuickGraphsScatter::updateLightStrength()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter19updateLightStrengthEv(
    QQuickGraphsScatter *self) {
  static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::updateLightStrength();
}

//  void QQuickGraphsScatter::startRecordingRemovesAndInserts()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter31startRecordingRemovesAndInsertsEv(
    QQuickGraphsScatter *self) {
  static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::startRecordingRemovesAndInserts();
}

//  QAbstract3DAxis
//      *QQuickGraphsScatter::getSeriesMultiAxis(QAbstract3DSeries *series,
//      QAbstract3DAxis::AxisOrientation orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN19QQuickGraphsScatter18getSeriesMultiAxisEP17QAbstract3DSeriesN15QAbstract3DAxis15AxisOrientationE(
    QQuickGraphsScatter *self,
    QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnQQuickGraphsScatter *>(self)->OwnQQuickGraphsScatter::getSeriesMultiAxis(
      series,
      orientation);
}

//  void QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(bool
//      visible, QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter37handleItemLabelVisibleChangedBySenderEbP7QObject(
    QQuickGraphsScatter *self,
    bool visible,
    QObject *sender) {
  self->QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(
      visible,
      sender);
}

//  void QQuickGraphsScatter::updateGraph()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter11updateGraphEv(
    QQuickGraphsScatter *self) {
  self->QQuickGraphsScatter::updateGraph();
}

//  void QQuickGraphsScatter::synchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter9synchDataEv(
    QQuickGraphsScatter *self) {
  self->QQuickGraphsScatter::synchData();
}

//  void QQuickGraphsScatter::handleOptimizationHintChange(QtGraphs3D::Optimi
//      zationHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter28handleOptimizationHintChangeEN10QtGraphs3D16OptimizationHintE(
    QQuickGraphsScatter *self,
    QtGraphs3D::OptimizationHint hint) {
  self->QQuickGraphsScatter::handleOptimizationHintChange(hint);
}

//  void QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickGraphsScatter37handleSeriesVisibilityChangedBySenderEP7QObject(
    QQuickGraphsScatter *self,
    QObject *sender) {
  self->QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(sender);
}

//  a QQmlListProperty<QScatter3DSeries> a ritual of QQuickGraphsScatter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGraphsScatter__QQmlListProperty_QScatter3DSeries(
    QQmlListProperty<QScatter3DSeries> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
