//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtextbrowser.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
#include <QtWidgets/qtextbrowser.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTextBrowser may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTextBrowser : QTextBrowser {
  using QTextBrowser::event;
  using QTextBrowser::keyPressEvent;
  using QTextBrowser::mouseMoveEvent;
  using QTextBrowser::mousePressEvent;
  using QTextBrowser::mouseReleaseEvent;
  using QTextBrowser::focusOutEvent;
  using QTextBrowser::focusNextPrevChild;
  using QTextBrowser::paintEvent;
  using QTextBrowser::doSetSource;
};

//  A QTextBrowser that Python can take functions over in. Every QTextBrowser
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textedit)
#if QT_CONFIG(textbrowser)
typedef const QVariant * (*CuteQTextBrowserCall0)(const void *, int, const QUrl *, int *);
#endif  // QT_CONFIG(textbrowser)
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall1)(const void *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall2)(const void *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall3)(const void *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall4)(const void *, int *);
#endif  // QT_CONFIG(textbrowser)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textbrowser)
typedef bool (*CuteQTextBrowserCall5)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall6)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall7)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall10)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef bool (*CuteQTextBrowserCall11)(const void *, bool, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall12)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
typedef void (*CuteQTextBrowserCall13)(const void *, const QUrl *, int, int *);
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textedit)
typedef const QVariant * (*CuteQTextBrowserCall14)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall15)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall16)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall17)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall18)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall19)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall20)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall21)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall22)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall23)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall24)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall25)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall26)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall27)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
typedef void * (*CuteQTextBrowserCall28)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef bool (*CuteQTextBrowserCall29)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall30)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall31)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall32)(const void *, int, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextBrowserCall33)(const void *, const QTextCursor *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTextBrowserCall34)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTextBrowserCall35)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTextBrowserCall36)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTextBrowserCall37)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTextBrowserCall38)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTextBrowserCall39)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTextBrowserCall40)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTextBrowserCall41)(const void *, int *);
typedef void (*CuteQTextBrowserCall42)(const void *, bool, int *);
typedef int (*CuteQTextBrowserCall43)(const void *, int, int *);
typedef bool (*CuteQTextBrowserCall44)(const void *, int *);
typedef void * (*CuteQTextBrowserCall45)(const void *, int *);
typedef void (*CuteQTextBrowserCall46)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTextBrowserCall47)(const void *, QEvent *, int *);
typedef void (*CuteQTextBrowserCall48)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTextBrowserCall49)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQTextBrowserCall50)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQTextBrowserCall51)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQTextBrowserCall52)(const void *, QHideEvent *, int *);
typedef int (*CuteQTextBrowserCall53)(const void *, int, int *);
typedef void (*CuteQTextBrowserCall54)(const void *, QPainter *, int *);
typedef void * (*CuteQTextBrowserCall55)(const void *, QPoint *, int *);
typedef void * (*CuteQTextBrowserCall56)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextBrowserCall57)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextBrowserCall58)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextBrowserCall59)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextBrowserCall60)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextBrowser : public QTextBrowser {
public:
  using QTextBrowser::QTextBrowser;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textedit)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN9QTextEdit12loadResourceEiRK4QUrl")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN12QTextBrowser8backwardEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN12QTextBrowser7forwardEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN12QTextBrowser4homeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN12QTextBrowser6reloadEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textbrowser)
    if (!std::strcmp(key, "_ZN12QTextBrowser11doSetSourceERK4QUrlN13QTextDocument12ResourceTypeE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK9QTextEdit27createMimeDataFromSelectionEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK9QTextEdit21canInsertFromMimeDataEPK9QMimeData")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit18insertFromMimeDataEPK9QMimeData")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit15doSetTextCursorERK11QTextCursor")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[49] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[56] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[59] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[60] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(textedit)
#if QT_CONFIG(textbrowser)
  //  QVariant QTextBrowser::loadResource(int type, const QUrl &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextBrowserCall0 call = reinterpret_cast<CuteQTextBrowserCall0>(taken[0]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QTextBrowser::loadResource(type, name);
  }
#endif  // QT_CONFIG(textbrowser)
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::backward()
  void backward() override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextBrowserCall1 call = reinterpret_cast<CuteQTextBrowserCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QTextBrowser::backward();
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::forward()
  void forward() override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextBrowserCall2 call = reinterpret_cast<CuteQTextBrowserCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QTextBrowser::forward();
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::home()
  void home() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextBrowserCall3 call = reinterpret_cast<CuteQTextBrowserCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTextBrowser::home();
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::reload()
  void reload() override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextBrowserCall4 call = reinterpret_cast<CuteQTextBrowserCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QTextBrowser::reload();
  }
#endif  // QT_CONFIG(textbrowser)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textbrowser)
  //  bool QTextBrowser::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextBrowserCall5 call = reinterpret_cast<CuteQTextBrowserCall5>(taken[5]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QTextBrowser::event(e);
  }
#endif  // QT_CONFIG(textbrowser)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextBrowserCall6 call = reinterpret_cast<CuteQTextBrowserCall6>(taken[6]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QTextBrowser::keyPressEvent(ev);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::mouseMoveEvent(QMouseEvent *ev)
  void mouseMoveEvent(QMouseEvent *ev) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextBrowserCall7 call = reinterpret_cast<CuteQTextBrowserCall7>(taken[7]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QTextBrowser::mouseMoveEvent(ev);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::mousePressEvent(QMouseEvent *ev)
  void mousePressEvent(QMouseEvent *ev) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextBrowserCall8 call = reinterpret_cast<CuteQTextBrowserCall8>(taken[8]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QTextBrowser::mousePressEvent(ev);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::mouseReleaseEvent(QMouseEvent *ev)
  void mouseReleaseEvent(QMouseEvent *ev) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextBrowserCall9 call = reinterpret_cast<CuteQTextBrowserCall9>(taken[9]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QTextBrowser::mouseReleaseEvent(ev);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::focusOutEvent(QFocusEvent *ev)
  void focusOutEvent(QFocusEvent *ev) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTextBrowserCall10 call = reinterpret_cast<CuteQTextBrowserCall10>(taken[10]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QTextBrowser::focusOutEvent(ev);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  bool QTextBrowser::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTextBrowserCall11 call = reinterpret_cast<CuteQTextBrowserCall11>(taken[11]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QTextBrowser::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTextBrowserCall12 call = reinterpret_cast<CuteQTextBrowserCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextBrowser::paintEvent(e);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textbrowser)
  //  void QTextBrowser::doSetSource(const QUrl &name,
  //      QTextDocument::ResourceType type)
  void doSetSource(
      const QUrl &name,
      QTextDocument::ResourceType type) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTextBrowserCall13 call = reinterpret_cast<CuteQTextBrowserCall13>(taken[13]);
      call(this, &name, static_cast<int>(type), &handled);
      if (handled) return;
    }
    QTextBrowser::doSetSource(name, type);
  }
#endif  // QT_CONFIG(textbrowser)

#if QT_CONFIG(textedit)
  //  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTextBrowserCall14 call = reinterpret_cast<CuteQTextBrowserCall14>(taken[14]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QTextEdit::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(textedit)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
  //  void QTextEdit::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTextBrowserCall15 call = reinterpret_cast<CuteQTextBrowserCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::timerEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(textedit)
  //  void QTextEdit::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTextBrowserCall16 call = reinterpret_cast<CuteQTextBrowserCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTextBrowserCall17 call = reinterpret_cast<CuteQTextBrowserCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::resizeEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
  void mouseDoubleClickEvent(QMouseEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTextBrowserCall18 call = reinterpret_cast<CuteQTextBrowserCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseDoubleClickEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
  //  void QTextEdit::contextMenuEvent(QContextMenuEvent *e)
  void contextMenuEvent(QContextMenuEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTextBrowserCall19 call = reinterpret_cast<CuteQTextBrowserCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::contextMenuEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dragEnterEvent(QDragEnterEvent *e)
  void dragEnterEvent(QDragEnterEvent *e) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTextBrowserCall20 call = reinterpret_cast<CuteQTextBrowserCall20>(taken[20]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dragEnterEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTextBrowserCall21 call = reinterpret_cast<CuteQTextBrowserCall21>(taken[21]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTextBrowserCall22 call = reinterpret_cast<CuteQTextBrowserCall22>(taken[22]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
  //  void QTextEdit::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTextBrowserCall23 call = reinterpret_cast<CuteQTextBrowserCall23>(taken[23]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::dropEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(textedit)
  //  void QTextEdit::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTextBrowserCall24 call = reinterpret_cast<CuteQTextBrowserCall24>(taken[24]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::focusInEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTextBrowserCall25 call = reinterpret_cast<CuteQTextBrowserCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTextEdit::showEvent(a0);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTextBrowserCall26 call = reinterpret_cast<CuteQTextBrowserCall26>(taken[26]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::changeEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
  //  void QTextEdit::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTextBrowserCall27 call = reinterpret_cast<CuteQTextBrowserCall27>(taken[27]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::wheelEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(textedit)
  //  QMimeData *QTextEdit::createMimeDataFromSelection() const
  QMimeData *createMimeDataFromSelection() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQTextBrowserCall28 call = reinterpret_cast<CuteQTextBrowserCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QTextEdit::createMimeDataFromSelection();
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  bool QTextEdit::canInsertFromMimeData(const QMimeData *source) const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQTextBrowserCall29 call = reinterpret_cast<CuteQTextBrowserCall29>(taken[29]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QTextEdit::canInsertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::insertFromMimeData(const QMimeData *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[30]) {
      int handled = 0;
      CuteQTextBrowserCall30 call = reinterpret_cast<CuteQTextBrowserCall30>(taken[30]);
      call(this, source, &handled);
      if (handled) return;
    }
    QTextEdit::insertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTextBrowserCall31 call = reinterpret_cast<CuteQTextBrowserCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTextEdit::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
  //  void QTextEdit::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTextBrowserCall32 call = reinterpret_cast<CuteQTextBrowserCall32>(taken[32]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QTextEdit::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(textedit)
  //  void QTextEdit::doSetTextCursor(const QTextCursor &cursor)
  void doSetTextCursor(const QTextCursor &cursor) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTextBrowserCall33 call = reinterpret_cast<CuteQTextBrowserCall33>(taken[33]);
      call(this, &cursor, &handled);
      if (handled) return;
    }
    QTextEdit::doSetTextCursor(cursor);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQTextBrowserCall34 call = reinterpret_cast<CuteQTextBrowserCall34>(taken[34]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQTextBrowserCall35 call = reinterpret_cast<CuteQTextBrowserCall35>(taken[35]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[36]) {
      int handled = 0;
      CuteQTextBrowserCall36 call = reinterpret_cast<CuteQTextBrowserCall36>(taken[36]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTextBrowserCall37 call = reinterpret_cast<CuteQTextBrowserCall37>(taken[37]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
  bool viewportEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQTextBrowserCall38 call = reinterpret_cast<CuteQTextBrowserCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQTextBrowserCall39 call = reinterpret_cast<CuteQTextBrowserCall39>(taken[39]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQTextBrowserCall40 call = reinterpret_cast<CuteQTextBrowserCall40>(taken[40]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQTextBrowserCall41 call = reinterpret_cast<CuteQTextBrowserCall41>(taken[41]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTextBrowserCall42 call = reinterpret_cast<CuteQTextBrowserCall42>(taken[42]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQTextBrowserCall43 call = reinterpret_cast<CuteQTextBrowserCall43>(taken[43]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQTextBrowserCall44 call = reinterpret_cast<CuteQTextBrowserCall44>(taken[44]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQTextBrowserCall45 call = reinterpret_cast<CuteQTextBrowserCall45>(taken[45]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTextBrowserCall46 call = reinterpret_cast<CuteQTextBrowserCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTextBrowserCall47 call = reinterpret_cast<CuteQTextBrowserCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQTextBrowserCall48 call = reinterpret_cast<CuteQTextBrowserCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQTextBrowserCall49 call = reinterpret_cast<CuteQTextBrowserCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQTextBrowserCall50 call = reinterpret_cast<CuteQTextBrowserCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQTextBrowserCall51 call = reinterpret_cast<CuteQTextBrowserCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQTextBrowserCall52 call = reinterpret_cast<CuteQTextBrowserCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[53]) {
      int handled = 0;
      CuteQTextBrowserCall53 call = reinterpret_cast<CuteQTextBrowserCall53>(taken[53]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[54]) {
      int handled = 0;
      CuteQTextBrowserCall54 call = reinterpret_cast<CuteQTextBrowserCall54>(taken[54]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[55]) {
      int handled = 0;
      CuteQTextBrowserCall55 call = reinterpret_cast<CuteQTextBrowserCall55>(taken[55]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[56]) {
      int handled = 0;
      CuteQTextBrowserCall56 call = reinterpret_cast<CuteQTextBrowserCall56>(taken[56]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQTextBrowserCall57 call = reinterpret_cast<CuteQTextBrowserCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQTextBrowserCall58 call = reinterpret_cast<CuteQTextBrowserCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[59]) {
      int handled = 0;
      CuteQTextBrowserCall59 call = reinterpret_cast<CuteQTextBrowserCall59>(taken[59]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[60]) {
      int handled = 0;
      CuteQTextBrowserCall60 call = reinterpret_cast<CuteQTextBrowserCall60>(taken[60]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextBrowser::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QTextBrowser10metaObjectEv(
    const QTextBrowser *self) {
  return self->metaObject();
}

//  void *QTextBrowser::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QTextBrowser11qt_metacastEPKc(
    QTextBrowser *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTextBrowser::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QTextBrowser11qt_metacallEN11QMetaObject4CallEiPPv(
    QTextBrowser *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTextBrowser::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTextBrowser2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextBrowser::tr(s, c, n));
}

//  QTextBrowser::QTextBrowser(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextBrowser *ritual_ZN12QTextBrowserC1EP7QWidget(QWidget *parent) {
  return new CuteQTextBrowser(parent);
}

//  QTextBrowser::~QTextBrowser()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowserD1Ev(QTextBrowser *self) {
  delete self;
}

//  QUrl QTextBrowser::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QTextBrowser6sourceEv(const QTextBrowser *self) {
  return new QUrl(self->source());
}

//  QTextDocument::ResourceType QTextBrowser::sourceType() const
extern "C" Q_DECL_EXPORT
QTextDocument::ResourceType ritual_ZNK12QTextBrowser10sourceTypeEv(
    const QTextBrowser *self) {
  return self->sourceType();
}

//  QStringList QTextBrowser::searchPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QTextBrowser11searchPathsEv(
    const QTextBrowser *self) {
  return new QList<QString>(self->searchPaths());
}

//  void QTextBrowser::setSearchPaths(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser14setSearchPathsERK5QListI7QStringE(
    QTextBrowser *self,
    const QList<QString> *paths) {
  self->setSearchPaths(*paths);
}

//  QVariant QTextBrowser::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN12QTextBrowser12loadResourceEiRK4QUrl(
    QTextBrowser *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  bool QTextBrowser::isBackwardAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser19isBackwardAvailableEv(
    const QTextBrowser *self) {
  return self->isBackwardAvailable();
}

//  bool QTextBrowser::isForwardAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser18isForwardAvailableEv(
    const QTextBrowser *self) {
  return self->isForwardAvailable();
}

//  void QTextBrowser::clearHistory()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser12clearHistoryEv(QTextBrowser *self) {
  self->clearHistory();
}

//  QString QTextBrowser::historyTitle(int a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QTextBrowser12historyTitleEi(
    const QTextBrowser *self,
    int a0) {
  return new QString(self->historyTitle(a0));
}

//  QUrl QTextBrowser::historyUrl(int a0) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QTextBrowser10historyUrlEi(
    const QTextBrowser *self,
    int a0) {
  return new QUrl(self->historyUrl(a0));
}

//  int QTextBrowser::backwardHistoryCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTextBrowser20backwardHistoryCountEv(
    const QTextBrowser *self) {
  return self->backwardHistoryCount();
}

//  int QTextBrowser::forwardHistoryCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTextBrowser19forwardHistoryCountEv(
    const QTextBrowser *self) {
  return self->forwardHistoryCount();
}

//  bool QTextBrowser::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser17openExternalLinksEv(
    const QTextBrowser *self) {
  return self->openExternalLinks();
}

//  void QTextBrowser::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser20setOpenExternalLinksEb(
    QTextBrowser *self,
    bool open) {
  self->setOpenExternalLinks(open);
}

//  bool QTextBrowser::openLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTextBrowser9openLinksEv(const QTextBrowser *self) {
  return self->openLinks();
}

//  void QTextBrowser::setOpenLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser12setOpenLinksEb(QTextBrowser *self, bool open) {
  self->setOpenLinks(open);
}

//  void QTextBrowser::setSource(const QUrl &name,
//      QTextDocument::ResourceType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser9setSourceERK4QUrlN13QTextDocument12ResourceTypeE(
    QTextBrowser *self,
    const QUrl *name,
    QTextDocument::ResourceType type) {
  self->setSource(*name, type);
}

//  void QTextBrowser::backward()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser8backwardEv(QTextBrowser *self) {
  self->backward();
}

//  void QTextBrowser::forward()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser7forwardEv(QTextBrowser *self) {
  self->forward();
}

//  void QTextBrowser::home()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser4homeEv(QTextBrowser *self) {
  self->home();
}

//  void QTextBrowser::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser6reloadEv(QTextBrowser *self) {
  self->reload();
}

//  void QTextBrowser::backwardAvailable(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser17backwardAvailableEb(
    QTextBrowser *self,
    bool a0) {
  self->backwardAvailable(a0);
}

//  void QTextBrowser::forwardAvailable(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser16forwardAvailableEb(
    QTextBrowser *self,
    bool a0) {
  self->forwardAvailable(a0);
}

//  void QTextBrowser::historyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser14historyChangedEv(QTextBrowser *self) {
  self->historyChanged();
}

//  void QTextBrowser::sourceChanged(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser13sourceChangedERK4QUrl(
    QTextBrowser *self,
    const QUrl *a0) {
  self->sourceChanged(*a0);
}

//  void QTextBrowser::highlighted(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser11highlightedERK4QUrl(
    QTextBrowser *self,
    const QUrl *a0) {
  self->highlighted(*a0);
}

//  void QTextBrowser::anchorClicked(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser13anchorClickedERK4QUrl(
    QTextBrowser *self,
    const QUrl *a0) {
  self->anchorClicked(*a0);
}

//  bool QTextBrowser::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QTextBrowser5eventEP6QEvent(QTextBrowser *self, QEvent *e) {
  return self->event(e);
}

//  void QTextBrowser::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser13keyPressEventEP9QKeyEvent(
    QTextBrowser *self,
    QKeyEvent *ev) {
  self->keyPressEvent(ev);
}

//  void QTextBrowser::mouseMoveEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser14mouseMoveEventEP11QMouseEvent(
    QTextBrowser *self,
    QMouseEvent *ev) {
  self->mouseMoveEvent(ev);
}

//  void QTextBrowser::mousePressEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser15mousePressEventEP11QMouseEvent(
    QTextBrowser *self,
    QMouseEvent *ev) {
  self->mousePressEvent(ev);
}

//  void QTextBrowser::mouseReleaseEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser17mouseReleaseEventEP11QMouseEvent(
    QTextBrowser *self,
    QMouseEvent *ev) {
  self->mouseReleaseEvent(ev);
}

//  void QTextBrowser::focusOutEvent(QFocusEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser13focusOutEventEP11QFocusEvent(
    QTextBrowser *self,
    QFocusEvent *ev) {
  self->focusOutEvent(ev);
}

//  bool QTextBrowser::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QTextBrowser18focusNextPrevChildEb(
    QTextBrowser *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  void QTextBrowser::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser10paintEventEP11QPaintEvent(
    QTextBrowser *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QTextBrowser::doSetSource(const QUrl &name,
//      QTextDocument::ResourceType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBrowser11doSetSourceERK4QUrlN13QTextDocument12ResourceTypeE(
    QTextBrowser *self,
    const QUrl *name,
    QTextDocument::ResourceType type) {
  self->doSetSource(*name, type);
}

//  QTextBrowserPrivate *QTextBrowser::d_func()
extern "C" Q_DECL_EXPORT
QTextBrowserPrivate *ritual_ZN12QTextBrowser6d_funcEv(QTextBrowser *self) {
  return self->d_func();
}

//  const QTextBrowserPrivate *QTextBrowser::d_func() const
extern "C" Q_DECL_EXPORT
const QTextBrowserPrivate *ritual_ZNK12QTextBrowser6d_funcEv(
    const QTextBrowser *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTextBrowser, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextBrowser(
    QTextBrowser *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextBrowser *>(self)->take(key, call);
}

//  QVariant QTextBrowser::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN12QTextBrowser12loadResourceEiRK4QUrl(
    QTextBrowser *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->QTextBrowser::loadResource(type, *name));
}

//  void QTextBrowser::backward()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser8backwardEv(QTextBrowser *self) {
  self->QTextBrowser::backward();
}

//  void QTextBrowser::forward()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser7forwardEv(QTextBrowser *self) {
  self->QTextBrowser::forward();
}

//  void QTextBrowser::home()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser4homeEv(QTextBrowser *self) {
  self->QTextBrowser::home();
}

//  void QTextBrowser::reload()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser6reloadEv(QTextBrowser *self) {
  self->QTextBrowser::reload();
}

//  bool QTextBrowser::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QTextBrowser5eventEP6QEvent(
    QTextBrowser *self,
    QEvent *e) {
  return static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::event(e);
}

//  void QTextBrowser::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser13keyPressEventEP9QKeyEvent(
    QTextBrowser *self,
    QKeyEvent *ev) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::keyPressEvent(ev);
}

//  void QTextBrowser::mouseMoveEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser14mouseMoveEventEP11QMouseEvent(
    QTextBrowser *self,
    QMouseEvent *ev) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::mouseMoveEvent(ev);
}

//  void QTextBrowser::mousePressEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser15mousePressEventEP11QMouseEvent(
    QTextBrowser *self,
    QMouseEvent *ev) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::mousePressEvent(ev);
}

//  void QTextBrowser::mouseReleaseEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser17mouseReleaseEventEP11QMouseEvent(
    QTextBrowser *self,
    QMouseEvent *ev) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::mouseReleaseEvent(
      ev);
}

//  void QTextBrowser::focusOutEvent(QFocusEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser13focusOutEventEP11QFocusEvent(
    QTextBrowser *self,
    QFocusEvent *ev) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::focusOutEvent(ev);
}

//  bool QTextBrowser::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QTextBrowser18focusNextPrevChildEb(
    QTextBrowser *self,
    bool next) {
  return static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::focusNextPrevChild(
      next);
}

//  void QTextBrowser::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser10paintEventEP11QPaintEvent(
    QTextBrowser *self,
    QPaintEvent *e) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::paintEvent(e);
}

//  void QTextBrowser::doSetSource(const QUrl &name,
//      QTextDocument::ResourceType type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTextBrowser11doSetSourceERK4QUrlN13QTextDocument12ResourceTypeE(
    QTextBrowser *self,
    const QUrl *name,
    QTextDocument::ResourceType type) {
  static_cast<OwnQTextBrowser *>(self)->OwnQTextBrowser::doSetSource(
      *name,
      type);
}

#endif  // QT_CONFIG(textbrowser)
#endif  // QT_CONFIG(textbrowser)
