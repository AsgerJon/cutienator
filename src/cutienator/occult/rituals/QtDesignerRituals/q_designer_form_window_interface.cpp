//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerFormWindowInterface that Python can take functions over in. Every QDesignerFormWindowInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerFormWindowInterfaceCall0)(const void *, int *);
typedef const QDir * (*CuteQDesignerFormWindowInterfaceCall1)(const void *, int *);
typedef QString * (*CuteQDesignerFormWindowInterfaceCall2)(const void *, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall3)(const void *, QIODevice *, QString *, int *);
typedef int (*CuteQDesignerFormWindowInterfaceCall4)(const void *, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall5)(const void *, int, int *);
typedef QString * (*CuteQDesignerFormWindowInterfaceCall6)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall7)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerFormWindowInterfaceCall8)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall9)(const void *, const QString *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall10)(const void *, int, int, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall11)(const void *, QString *, QString *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall12)(const void *, const QString *, const QString *, int *);
typedef QString * (*CuteQDesignerFormWindowInterfaceCall13)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall14)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerFormWindowInterfaceCall15)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall16)(const void *, const QString *, int *);
typedef int (*CuteQDesignerFormWindowInterfaceCall17)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall18)(const void *, int, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall19)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall20)(const void *, QtResourceSet *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall21)(const void *, int *);
#if !defined(QT_NO_CURSOR)
typedef void * (*CuteQDesignerFormWindowInterfaceCall22)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
typedef int (*CuteQDesignerFormWindowInterfaceCall23)(const void *, int *);
typedef int (*CuteQDesignerFormWindowInterfaceCall24)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall25)(const void *, int, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall26)(const void *, int, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall27)(const void *, QDesignerFormWindowToolInterface *, int *);
typedef const QPoint * (*CuteQDesignerFormWindowInterfaceCall28)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall29)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall30)(const void *, QWidget *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall31)(const void *, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall32)(const void *, QWidget *, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall33)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall34)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall35)(const void *, const QString *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall36)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall37)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall38)(const void *, const QString *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall39)(const void *, const QString *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall40)(const void *, QObject *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall41)(const void *, QWidget *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall42)(const void *, QWidget *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall43)(const void *, int, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall44)(const void *, bool, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall45)(const void *, bool, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall46)(const void *, QWidget *, bool, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall47)(const void *, const QPoint *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall48)(const void *, const QString *, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall49)(const void *, const QString *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall50)(const void *, int *);
typedef int (*CuteQDesignerFormWindowInterfaceCall51)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall52)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerFormWindowInterfaceCall53)(const void *, int *);
typedef const QSize * (*CuteQDesignerFormWindowInterfaceCall54)(const void *, int *);
typedef int (*CuteQDesignerFormWindowInterfaceCall55)(const void *, int, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall56)(const void *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall57)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormWindowInterfaceCall58)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowInterfaceCall59)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall60)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall61)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall62)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerFormWindowInterfaceCall63)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerFormWindowInterfaceCall64)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall65)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall66)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall67)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall68)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall69)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall70)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall71)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall72)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall73)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerFormWindowInterfaceCall74)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerFormWindowInterfaceCall75)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerFormWindowInterfaceCall76)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerFormWindowInterfaceCall77)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerFormWindowInterfaceCall78)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerFormWindowInterfaceCall79)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerFormWindowInterfaceCall80)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerFormWindowInterfaceCall81)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall82)(const void *, QHideEvent *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall83)(const void *, QEvent *, int *);
typedef int (*CuteQDesignerFormWindowInterfaceCall84)(const void *, int, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall85)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall86)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerFormWindowInterfaceCall87)(const void *, int *);
typedef void (*CuteQDesignerFormWindowInterfaceCall88)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerFormWindowInterfaceCall89)(const void *, int, int *);
typedef bool (*CuteQDesignerFormWindowInterfaceCall90)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerFormWindowInterfaceCall91)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowInterfaceCall92)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowInterfaceCall93)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowInterfaceCall94)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowInterfaceCall95)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerFormWindowInterfaceCall96)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerFormWindowInterface : public QDesignerFormWindowInterface {
public:
  using QDesignerFormWindowInterface::QDesignerFormWindowInterface;
  void *taken[97] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface8fileNameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11absoluteDirEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface8contentsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setContentsEP9QIODeviceP7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface8featuresEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface10hasFeatureE6QFlagsINS_11FeatureFlagEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface6authorEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface9setAuthorERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface7commentEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface10setCommentERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface16setLayoutDefaultEii")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14layoutFunctionEP7QStringS1_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface17setLayoutFunctionERK7QStringS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface14pixmapFunctionEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface17setPixmapFunctionERK7QString")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11exportMacroEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14setExportMacroERK7QString")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface20resourceFileSaveModeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface23setResourceFileSaveModeENS_20ResourceFileSaveModeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11resourceSetEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14setResourceSetEP13QtResourceSet")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface4coreEv")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK7QWidget6cursorEv")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface9toolCountEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface11currentToolEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14setCurrentToolEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface4toolEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12registerToolEP32QDesignerFormWindowToolInterface")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface4gridEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface13mainContainerEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface16setMainContainerEP7QWidget")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface13formContainerEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface9isManagedEP7QWidget")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface7isDirtyEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerFormWindowInterface14commandHistoryEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12beginCommandERK7QString")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface10endCommandEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface20emitSelectionChangedEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface15addResourceFileERK7QString")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface18removeResourceFileERK7QString")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface22ensureUniqueObjectNameEP7QObject")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12manageWidgetEP7QWidget")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14unmanageWidgetEP7QWidget")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setFeaturesE6QFlagsINS_11FeatureFlagEE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface8setDirtyEb")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface14clearSelectionEb")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface12selectWidgetEP7QWidgetb")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface7setGridERK6QPoint")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setFileNameERK7QString")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11setContentsERK7QString")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QDesignerFormWindowInterface11editWidgetsEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[57] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[62] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[63] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[73] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[74] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[75] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[76] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[77] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[78] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[79] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[80] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[90] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[91] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[92] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[93] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[94] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[95] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[96] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QString QDesignerFormWindowInterface::fileName() const
  QString fileName() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall0 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QDir QDesignerFormWindowInterface::absoluteDir() const
  QDir absoluteDir() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall1 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall1>(taken[1]);
      const QDir * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QString QDesignerFormWindowInterface::contents() const
  QString contents() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall2 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::setContents(QIODevice *dev,
  //      QString *errorMessage)
  bool setContents(QIODevice *dev, QString *errorMessage) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall3 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall3>(taken[3]);
      bool given = call(this, dev, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Feature QDesignerFormWindowInterface::features() const
  QDesignerFormWindowInterface::Feature features() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall4 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(given);
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::hasFeature(Feature f) const
  bool hasFeature(QDesignerFormWindowInterface::Feature f) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall5 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall5>(taken[5]);
      bool given = call(this, static_cast<int>(f.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerFormWindowInterface::author() const
  QString author() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall6 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setAuthor(const QString &author)
  void setAuthor(const QString &author) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall7 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall7>(taken[7]);
      call(this, &author, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerFormWindowInterface::comment() const
  QString comment() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall8 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setComment(const QString &comment)
  void setComment(const QString &comment) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall9 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall9>(taken[9]);
      call(this, &comment, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setLayoutDefault(int margin, int
  //      spacing)
  void setLayoutDefault(int margin, int spacing) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall10 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall10>(taken[10]);
      call(this, margin, spacing, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::layoutFunction(QString *margin,
  //      QString *spacing)
  void layoutFunction(QString *margin, QString *spacing) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall11 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall11>(taken[11]);
      call(this, margin, spacing, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setLayoutFunction(const QString
  //      &margin, const QString &spacing)
  void setLayoutFunction(
      const QString &margin,
      const QString &spacing) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall12 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall12>(taken[12]);
      call(this, &margin, &spacing, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerFormWindowInterface::pixmapFunction() const
  QString pixmapFunction() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall13 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall13>(taken[13]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setPixmapFunction(const QString
  //      &pixmapFunction)
  void setPixmapFunction(const QString &pixmapFunction) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall14 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall14>(taken[14]);
      call(this, &pixmapFunction, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerFormWindowInterface::exportMacro() const
  QString exportMacro() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall15 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall15>(taken[15]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setExportMacro(const QString
  //      &exportMacro)
  void setExportMacro(const QString &exportMacro) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall16 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall16>(taken[16]);
      call(this, &exportMacro, &handled);
      if (handled) return;
    }
  }

  //  ResourceFileSaveMode
  //      QDesignerFormWindowInterface::resourceFileSaveMode() const
  QDesignerFormWindowInterface::ResourceFileSaveMode resourceFileSaveMode() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall17 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowInterface::ResourceFileSaveMode>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setResourceFileSaveMode(ResourceFi
  //      leSaveMode behaviour)
  void setResourceFileSaveMode(
      QDesignerFormWindowInterface::ResourceFileSaveMode behaviour) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall18 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall18>(taken[18]);
      call(this, static_cast<int>(behaviour), &handled);
      if (handled) return;
    }
  }

  //  QtResourceSet *QDesignerFormWindowInterface::resourceSet() const
  QtResourceSet *resourceSet() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall19 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QtResourceSet *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setResourceSet(QtResourceSet
  //      *resourceSet)
  void setResourceSet(QtResourceSet *resourceSet) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall20 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall20>(taken[20]);
      call(this, resourceSet, &handled);
      if (handled) return;
    }
  }

  //  QDesignerFormEditorInterface *QDesignerFormWindowInterface::core()
  //      const
  QDesignerFormEditorInterface *core() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall21 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return QDesignerFormWindowInterface::core();
  }

#if !defined(QT_NO_CURSOR)
  //  QDesignerFormWindowCursorInterface
  //      *QDesignerFormWindowInterface::cursor() const
  QDesignerFormWindowCursorInterface *cursor() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall22 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormWindowCursorInterface *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_CURSOR)

  //  int QDesignerFormWindowInterface::toolCount() const
  int toolCount() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall23 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerFormWindowInterface::currentTool() const
  int currentTool() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall24 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setCurrentTool(int index)
  void setCurrentTool(int index) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall25 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall25>(taken[25]);
      call(this, index, &handled);
      if (handled) return;
    }
  }

  //  QDesignerFormWindowToolInterface
  //      *QDesignerFormWindowInterface::tool(int index) const
  QDesignerFormWindowToolInterface *tool(int index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall26 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall26>(taken[26]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QDesignerFormWindowToolInterface *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::registerTool(QDesignerFormWindowTo
  //      olInterface *tool)
  void registerTool(QDesignerFormWindowToolInterface *tool) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall27 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall27>(taken[27]);
      call(this, tool, &handled);
      if (handled) return;
    }
  }

  //  QPoint QDesignerFormWindowInterface::grid() const
  QPoint grid() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall28 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall28>(taken[28]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QWidget *QDesignerFormWindowInterface::mainContainer() const
  QWidget *mainContainer() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall29 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::setMainContainer(QWidget
  //      *mainContainer)
  void setMainContainer(QWidget *mainContainer) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall30 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall30>(taken[30]);
      call(this, mainContainer, &handled);
      if (handled) return;
    }
  }

  //  QWidget *QDesignerFormWindowInterface::formContainer() const
  QWidget *formContainer() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall31 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::isManaged(QWidget *widget) const
  bool isManaged(QWidget *widget) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall32 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall32>(taken[32]);
      bool given = call(this, widget, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerFormWindowInterface::isDirty() const
  bool isDirty() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall33 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall33>(taken[33]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QUndoStack *QDesignerFormWindowInterface::commandHistory() const
  QUndoStack *commandHistory() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall34 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall34>(taken[34]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QUndoStack *>(given);
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::beginCommand(const QString
  //      &description)
  void beginCommand(const QString &description) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall35 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall35>(taken[35]);
      call(this, &description, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::endCommand()
  void endCommand() override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall36 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::emitSelectionChanged()
  void emitSelectionChanged() override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall37 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::addResourceFile(const QString
  //      &path)
  void addResourceFile(const QString &path) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall38 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall38>(taken[38]);
      call(this, &path, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::removeResourceFile(const QString
  //      &path)
  void removeResourceFile(const QString &path) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall39 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall39>(taken[39]);
      call(this, &path, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::ensureUniqueObjectName(QObject
  //      *object)
  void ensureUniqueObjectName(QObject *object) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall40 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall40>(taken[40]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::manageWidget(QWidget *widget)
  void manageWidget(QWidget *widget) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall41 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall41>(taken[41]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::unmanageWidget(QWidget *widget)
  void unmanageWidget(QWidget *widget) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall42 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall42>(taken[42]);
      call(this, widget, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setFeatures(Feature f)
  void setFeatures(QDesignerFormWindowInterface::Feature f) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall43 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall43>(taken[43]);
      call(this, static_cast<int>(f.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setDirty(bool dirty)
  void setDirty(bool dirty) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall44 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall44>(taken[44]);
      call(this, dirty, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::clearSelection(bool
  //      changePropertyDisplay)
  void clearSelection(bool changePropertyDisplay) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall45 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall45>(taken[45]);
      call(this, changePropertyDisplay, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::selectWidget(QWidget *w, bool
  //      select)
  void selectWidget(QWidget *w, bool select) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall46 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall46>(taken[46]);
      call(this, w, select, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setGrid(const QPoint &grid)
  void setGrid(const QPoint &grid) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall47 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall47>(taken[47]);
      call(this, &grid, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerFormWindowInterface::setFileName(const QString
  //      &fileName)
  void setFileName(const QString &fileName) override {
    if (taken[48]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall48 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall48>(taken[48]);
      call(this, &fileName, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerFormWindowInterface::setContents(const QString
  //      &contents)
  bool setContents(const QString &contents) override {
    if (taken[49]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall49 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall49>(taken[49]);
      bool given = call(this, &contents, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerFormWindowInterface::editWidgets()
  void editWidgets() override {
    if (taken[50]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall50 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[51]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall51 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall51>(taken[51]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[52]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall52 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall52>(taken[52]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[53]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall53 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall53>(taken[53]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall54 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall54>(taken[54]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[55]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall55 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall55>(taken[55]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[56]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall56 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall56>(taken[56]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[57]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall57 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall57>(taken[57]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall58 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall58>(taken[58]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall59 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall59>(taken[59]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[60]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall60 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall60>(taken[60]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[61]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall61 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall61>(taken[61]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[62]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall62 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall62>(taken[62]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[63]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall63 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall63>(taken[63]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[64]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall64 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall64>(taken[64]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[65]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall65 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall65>(taken[65]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[66]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall66 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall66>(taken[66]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[67]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall67 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall67>(taken[67]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[68]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall68 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall68>(taken[68]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[69]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall69 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall69>(taken[69]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall70 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall71 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall72 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall73 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall74 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall75 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall76 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall77 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall78 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[79]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall79 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[80]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall80 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall80>(taken[80]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[81]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall81 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall81>(taken[81]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[82]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall82 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall82>(taken[82]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall83 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall83>(taken[83]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[84]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall84 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall84>(taken[84]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[85]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall85 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall85>(taken[85]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[86]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall86 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall86>(taken[86]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[87]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall87 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall87>(taken[87]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall88 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall88>(taken[88]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[89]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall89 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall89>(taken[89]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[90]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall90 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall90>(taken[90]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[91]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall91 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall91>(taken[91]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[92]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall92 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall92>(taken[92]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[93]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall93 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall93>(taken[93]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[94]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall94 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall94>(taken[94]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[95]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall95 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall95>(taken[95]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[96]) {
      int handled = 0;
      CuteQDesignerFormWindowInterfaceCall96 call = reinterpret_cast<CuteQDesignerFormWindowInterfaceCall96>(taken[96]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerFormWindowInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QDesignerFormWindowInterface10metaObjectEv(
    const QDesignerFormWindowInterface *self) {
  return self->metaObject();
}

//  QString QDesignerFormWindowInterface::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QDesignerFormWindowInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerFormWindowInterface::tr(s, c, n));
}

//  QDesignerFormWindowInterface::~QDesignerFormWindowInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterfaceD1Ev(
    QDesignerFormWindowInterface *self) {
  delete self;
}

//  QString QDesignerFormWindowInterface::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormWindowInterface8fileNameEv(
    const QDesignerFormWindowInterface *self) {
  return new QString(self->fileName());
}

//  QDir QDesignerFormWindowInterface::absoluteDir() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK28QDesignerFormWindowInterface11absoluteDirEv(
    const QDesignerFormWindowInterface *self) {
  return new QDir(self->absoluteDir());
}

//  QString QDesignerFormWindowInterface::contents() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormWindowInterface8contentsEv(
    const QDesignerFormWindowInterface *self) {
  return new QString(self->contents());
}

//  QStringList QDesignerFormWindowInterface::checkContents() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QDesignerFormWindowInterface13checkContentsEv(
    const QDesignerFormWindowInterface *self) {
  return new QList<QString>(self->checkContents());
}

//  bool QDesignerFormWindowInterface::setContents(QIODevice *dev, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QDesignerFormWindowInterface11setContentsEP9QIODeviceP7QString(
    QDesignerFormWindowInterface *self,
    QIODevice *dev,
    QString *errorMessage) {
  return self->setContents(dev, errorMessage);
}

//  Feature QDesignerFormWindowInterface::features() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerFormWindowInterface8featuresEv(
    const QDesignerFormWindowInterface *self) {
  return static_cast<int>(self->features().toInt());
}

//  bool QDesignerFormWindowInterface::hasFeature(Feature f) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QDesignerFormWindowInterface10hasFeatureE6QFlagsINS_11FeatureFlagEE(
    const QDesignerFormWindowInterface *self,
    int f) {
  return self->hasFeature(
      QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(f));
}

//  QString QDesignerFormWindowInterface::author() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormWindowInterface6authorEv(
    const QDesignerFormWindowInterface *self) {
  return new QString(self->author());
}

//  void QDesignerFormWindowInterface::setAuthor(const QString &author)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface9setAuthorERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *author) {
  self->setAuthor(*author);
}

//  QString QDesignerFormWindowInterface::comment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormWindowInterface7commentEv(
    const QDesignerFormWindowInterface *self) {
  return new QString(self->comment());
}

//  void QDesignerFormWindowInterface::setComment(const QString &comment)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface10setCommentERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *comment) {
  self->setComment(*comment);
}

//  void QDesignerFormWindowInterface::layoutDefault(int *margin, int
//      *spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface13layoutDefaultEPiS0_(
    QDesignerFormWindowInterface *self,
    int *margin,
    int *spacing) {
  self->layoutDefault(margin, spacing);
}

//  void QDesignerFormWindowInterface::setLayoutDefault(int margin, int
//      spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface16setLayoutDefaultEii(
    QDesignerFormWindowInterface *self,
    int margin,
    int spacing) {
  self->setLayoutDefault(margin, spacing);
}

//  void QDesignerFormWindowInterface::layoutFunction(QString *margin,
//      QString *spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface14layoutFunctionEP7QStringS1_(
    QDesignerFormWindowInterface *self,
    QString *margin,
    QString *spacing) {
  self->layoutFunction(margin, spacing);
}

//  void QDesignerFormWindowInterface::setLayoutFunction(const QString
//      &margin, const QString &spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface17setLayoutFunctionERK7QStringS2_(
    QDesignerFormWindowInterface *self,
    const QString *margin,
    const QString *spacing) {
  self->setLayoutFunction(*margin, *spacing);
}

//  QString QDesignerFormWindowInterface::pixmapFunction() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormWindowInterface14pixmapFunctionEv(
    const QDesignerFormWindowInterface *self) {
  return new QString(self->pixmapFunction());
}

//  void QDesignerFormWindowInterface::setPixmapFunction(const QString
//      &pixmapFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface17setPixmapFunctionERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *pixmapFunction) {
  self->setPixmapFunction(*pixmapFunction);
}

//  QString QDesignerFormWindowInterface::exportMacro() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerFormWindowInterface11exportMacroEv(
    const QDesignerFormWindowInterface *self) {
  return new QString(self->exportMacro());
}

//  void QDesignerFormWindowInterface::setExportMacro(const QString
//      &exportMacro)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface14setExportMacroERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *exportMacro) {
  self->setExportMacro(*exportMacro);
}

//  QStringList QDesignerFormWindowInterface::includeHints() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QDesignerFormWindowInterface12includeHintsEv(
    const QDesignerFormWindowInterface *self) {
  return new QList<QString>(self->includeHints());
}

//  void QDesignerFormWindowInterface::setIncludeHints(const QStringList
//      &includeHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface15setIncludeHintsERK5QListI7QStringE(
    QDesignerFormWindowInterface *self,
    const QList<QString> *includeHints) {
  self->setIncludeHints(*includeHints);
}

//  ResourceFileSaveMode QDesignerFormWindowInterface::resourceFileSaveMode()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface::ResourceFileSaveMode ritual_ZNK28QDesignerFormWindowInterface20resourceFileSaveModeEv(
    const QDesignerFormWindowInterface *self) {
  return self->resourceFileSaveMode();
}

//  void QDesignerFormWindowInterface::setResourceFileSaveMode(ResourceFileSa
//      veMode behaviour)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface23setResourceFileSaveModeENS_20ResourceFileSaveModeE(
    QDesignerFormWindowInterface *self,
    QDesignerFormWindowInterface::ResourceFileSaveMode behaviour) {
  self->setResourceFileSaveMode(behaviour);
}

//  QtResourceSet *QDesignerFormWindowInterface::resourceSet() const
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZNK28QDesignerFormWindowInterface11resourceSetEv(
    const QDesignerFormWindowInterface *self) {
  return self->resourceSet();
}

//  void QDesignerFormWindowInterface::setResourceSet(QtResourceSet
//      *resourceSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface14setResourceSetEP13QtResourceSet(
    QDesignerFormWindowInterface *self,
    QtResourceSet *resourceSet) {
  self->setResourceSet(resourceSet);
}

//  QStringList QDesignerFormWindowInterface::activeResourceFilePaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QDesignerFormWindowInterface23activeResourceFilePathsEv(
    const QDesignerFormWindowInterface *self) {
  return new QList<QString>(self->activeResourceFilePaths());
}

//  QDesignerFormEditorInterface *QDesignerFormWindowInterface::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK28QDesignerFormWindowInterface4coreEv(
    const QDesignerFormWindowInterface *self) {
  return self->core();
}

//  QDesignerFormWindowCursorInterface
//      *QDesignerFormWindowInterface::cursor() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowCursorInterface *ritual_ZNK28QDesignerFormWindowInterface6cursorEv(
    const QDesignerFormWindowInterface *self) {
  return self->cursor();
}

//  int QDesignerFormWindowInterface::toolCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerFormWindowInterface9toolCountEv(
    const QDesignerFormWindowInterface *self) {
  return self->toolCount();
}

//  int QDesignerFormWindowInterface::currentTool() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerFormWindowInterface11currentToolEv(
    const QDesignerFormWindowInterface *self) {
  return self->currentTool();
}

//  void QDesignerFormWindowInterface::setCurrentTool(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface14setCurrentToolEi(
    QDesignerFormWindowInterface *self,
    int index) {
  self->setCurrentTool(index);
}

//  QDesignerFormWindowToolInterface *QDesignerFormWindowInterface::tool(int
//      index) const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowToolInterface *ritual_ZNK28QDesignerFormWindowInterface4toolEi(
    const QDesignerFormWindowInterface *self,
    int index) {
  return self->tool(index);
}

//  void QDesignerFormWindowInterface::registerTool(QDesignerFormWindowToolIn
//      terface *tool)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface12registerToolEP32QDesignerFormWindowToolInterface(
    QDesignerFormWindowInterface *self,
    QDesignerFormWindowToolInterface *tool) {
  self->registerTool(tool);
}

//  QPoint QDesignerFormWindowInterface::grid() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK28QDesignerFormWindowInterface4gridEv(
    const QDesignerFormWindowInterface *self) {
  return new QPoint(self->grid());
}

//  QWidget *QDesignerFormWindowInterface::mainContainer() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK28QDesignerFormWindowInterface13mainContainerEv(
    const QDesignerFormWindowInterface *self) {
  return self->mainContainer();
}

//  void QDesignerFormWindowInterface::setMainContainer(QWidget
//      *mainContainer)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface16setMainContainerEP7QWidget(
    QDesignerFormWindowInterface *self,
    QWidget *mainContainer) {
  self->setMainContainer(mainContainer);
}

//  QWidget *QDesignerFormWindowInterface::formContainer() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK28QDesignerFormWindowInterface13formContainerEv(
    const QDesignerFormWindowInterface *self) {
  return self->formContainer();
}

//  bool QDesignerFormWindowInterface::isManaged(QWidget *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QDesignerFormWindowInterface9isManagedEP7QWidget(
    const QDesignerFormWindowInterface *self,
    QWidget *widget) {
  return self->isManaged(widget);
}

//  bool QDesignerFormWindowInterface::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QDesignerFormWindowInterface7isDirtyEv(
    const QDesignerFormWindowInterface *self) {
  return self->isDirty();
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowInterface::findFormWindow(QWidget *w)
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZN28QDesignerFormWindowInterface14findFormWindowEP7QWidget(
    QWidget *w) {
  return QDesignerFormWindowInterface::findFormWindow(w);
}

//  QDesignerFormWindowInterface
//      *QDesignerFormWindowInterface::findFormWindow(QObject *obj)
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZN28QDesignerFormWindowInterface14findFormWindowEP7QObject(
    QObject *obj) {
  return QDesignerFormWindowInterface::findFormWindow(obj);
}

//  QUndoStack *QDesignerFormWindowInterface::commandHistory() const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZNK28QDesignerFormWindowInterface14commandHistoryEv(
    const QDesignerFormWindowInterface *self) {
  return self->commandHistory();
}

//  void QDesignerFormWindowInterface::beginCommand(const QString
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface12beginCommandERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *description) {
  self->beginCommand(*description);
}

//  void QDesignerFormWindowInterface::endCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface10endCommandEv(
    QDesignerFormWindowInterface *self) {
  self->endCommand();
}

//  void QDesignerFormWindowInterface::emitSelectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface20emitSelectionChangedEv(
    QDesignerFormWindowInterface *self) {
  self->emitSelectionChanged();
}

//  QStringList QDesignerFormWindowInterface::resourceFiles() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QDesignerFormWindowInterface13resourceFilesEv(
    const QDesignerFormWindowInterface *self) {
  return new QList<QString>(self->resourceFiles());
}

//  void QDesignerFormWindowInterface::addResourceFile(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface15addResourceFileERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *path) {
  self->addResourceFile(*path);
}

//  void QDesignerFormWindowInterface::removeResourceFile(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface18removeResourceFileERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *path) {
  self->removeResourceFile(*path);
}

//  void QDesignerFormWindowInterface::ensureUniqueObjectName(QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface22ensureUniqueObjectNameEP7QObject(
    QDesignerFormWindowInterface *self,
    QObject *object) {
  self->ensureUniqueObjectName(object);
}

//  void QDesignerFormWindowInterface::manageWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface12manageWidgetEP7QWidget(
    QDesignerFormWindowInterface *self,
    QWidget *widget) {
  self->manageWidget(widget);
}

//  void QDesignerFormWindowInterface::unmanageWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface14unmanageWidgetEP7QWidget(
    QDesignerFormWindowInterface *self,
    QWidget *widget) {
  self->unmanageWidget(widget);
}

//  void QDesignerFormWindowInterface::setFeatures(Feature f)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface11setFeaturesE6QFlagsINS_11FeatureFlagEE(
    QDesignerFormWindowInterface *self,
    int f) {
  self->setFeatures(
      QFlags<QDesignerFormWindowInterface::FeatureFlag>::fromInt(f));
}

//  void QDesignerFormWindowInterface::setDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface8setDirtyEb(
    QDesignerFormWindowInterface *self,
    bool dirty) {
  self->setDirty(dirty);
}

//  void QDesignerFormWindowInterface::clearSelection(bool
//      changePropertyDisplay)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface14clearSelectionEb(
    QDesignerFormWindowInterface *self,
    bool changePropertyDisplay) {
  self->clearSelection(changePropertyDisplay);
}

//  void QDesignerFormWindowInterface::selectWidget(QWidget *w, bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface12selectWidgetEP7QWidgetb(
    QDesignerFormWindowInterface *self,
    QWidget *w,
    bool select) {
  self->selectWidget(w, select);
}

//  void QDesignerFormWindowInterface::setGrid(const QPoint &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface7setGridERK6QPoint(
    QDesignerFormWindowInterface *self,
    const QPoint *grid) {
  self->setGrid(*grid);
}

//  void QDesignerFormWindowInterface::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface11setFileNameERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  bool QDesignerFormWindowInterface::setContents(const QString &contents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QDesignerFormWindowInterface11setContentsERK7QString(
    QDesignerFormWindowInterface *self,
    const QString *contents) {
  return self->setContents(*contents);
}

//  void QDesignerFormWindowInterface::editWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface11editWidgetsEv(
    QDesignerFormWindowInterface *self) {
  self->editWidgets();
}

//  void QDesignerFormWindowInterface::activateResourceFilePaths(const
//      QStringList &paths, int *errorCount, QString *errorMessages)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerFormWindowInterface25activateResourceFilePathsERK5QListI7QStringEPiPS1_(
    QDesignerFormWindowInterface *self,
    const QList<QString> *paths,
    int *errorCount,
    QString *errorMessages) {
  self->activateResourceFilePaths(*paths, errorCount, errorMessages);
}

//  a Python function taken by a CuteQDesignerFormWindowInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerFormWindowInterface *>(self)->take(key, call);
}

//  QDesignerFormEditorInterface *QDesignerFormWindowInterface::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK28QDesignerFormWindowInterface4coreEv(
    const QDesignerFormWindowInterface *self) {
  return self->QDesignerFormWindowInterface::core();
}
