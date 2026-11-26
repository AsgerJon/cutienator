//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
#include <QtWidgets/qtextedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtGui/qtextformat.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <QtWidgets/QTextEdit>

//  Only a class built on QTextEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTextEdit : QTextEdit {
  using QTextEdit::event;
  using QTextEdit::timerEvent;
  using QTextEdit::keyPressEvent;
  using QTextEdit::keyReleaseEvent;
  using QTextEdit::resizeEvent;
  using QTextEdit::paintEvent;
  using QTextEdit::mousePressEvent;
  using QTextEdit::mouseMoveEvent;
  using QTextEdit::mouseReleaseEvent;
  using QTextEdit::mouseDoubleClickEvent;
  using QTextEdit::focusNextPrevChild;
  using QTextEdit::contextMenuEvent;
  using QTextEdit::dragEnterEvent;
  using QTextEdit::dragLeaveEvent;
  using QTextEdit::dragMoveEvent;
  using QTextEdit::dropEvent;
  using QTextEdit::focusInEvent;
  using QTextEdit::focusOutEvent;
  using QTextEdit::showEvent;
  using QTextEdit::changeEvent;
  using QTextEdit::wheelEvent;
  using QTextEdit::createMimeDataFromSelection;
  using QTextEdit::canInsertFromMimeData;
  using QTextEdit::insertFromMimeData;
  using QTextEdit::inputMethodEvent;
  using QTextEdit::scrollContentsBy;
  using QTextEdit::doSetTextCursor;
};

//  A QTextEdit that Python can take functions over in. Every QTextEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textedit)
typedef const QVariant * (*CuteQTextEditCall0)(const void *, int, const QUrl *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef const QVariant * (*CuteQTextEditCall1)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef bool (*CuteQTextEditCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall3)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall4)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall5)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall6)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall7)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall10)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef bool (*CuteQTextEditCall12)(const void *, bool, int *);
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall14)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall15)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall16)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall17)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall18)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall20)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall21)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
typedef void * (*CuteQTextEditCall23)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef bool (*CuteQTextEditCall24)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall25)(const void *, const QMimeData *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall26)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall27)(const void *, int, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
typedef void (*CuteQTextEditCall28)(const void *, const QTextCursor *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTextEditCall29)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTextEditCall30)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTextEditCall31)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTextEditCall32)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTextEditCall33)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTextEditCall34)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTextEditCall35)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTextEditCall36)(const void *, int *);
typedef void (*CuteQTextEditCall37)(const void *, bool, int *);
typedef int (*CuteQTextEditCall38)(const void *, int, int *);
typedef bool (*CuteQTextEditCall39)(const void *, int *);
typedef void * (*CuteQTextEditCall40)(const void *, int *);
typedef void (*CuteQTextEditCall41)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTextEditCall42)(const void *, QEvent *, int *);
typedef void (*CuteQTextEditCall43)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTextEditCall44)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQTextEditCall45)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQTextEditCall46)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQTextEditCall47)(const void *, QHideEvent *, int *);
typedef int (*CuteQTextEditCall48)(const void *, int, int *);
typedef void (*CuteQTextEditCall49)(const void *, QPainter *, int *);
typedef void * (*CuteQTextEditCall50)(const void *, QPoint *, int *);
typedef void * (*CuteQTextEditCall51)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextEditCall52)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextEditCall53)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextEditCall54)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextEditCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextEdit : public QTextEdit {
public:
  using QTextEdit::QTextEdit;
  void *taken[56] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit12loadResourceEiRK4QUrl")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK9QTextEdit27createMimeDataFromSelectionEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK9QTextEdit21canInsertFromMimeDataEPK9QMimeData")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit18insertFromMimeDataEPK9QMimeData")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN9QTextEdit15doSetTextCursorERK11QTextCursor")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[44] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[51] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(textedit)
  //  QVariant QTextEdit::loadResource(int type, const QUrl &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextEditCall0 call = reinterpret_cast<CuteQTextEditCall0>(taken[0]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QTextEdit::loadResource(type, name);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextEditCall1 call = reinterpret_cast<CuteQTextEditCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QTextEdit::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(textedit)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
  //  bool QTextEdit::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextEditCall2 call = reinterpret_cast<CuteQTextEditCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QTextEdit::event(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(textedit)
  //  void QTextEdit::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextEditCall3 call = reinterpret_cast<CuteQTextEditCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::timerEvent(e);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(textedit)
  //  void QTextEdit::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextEditCall4 call = reinterpret_cast<CuteQTextEditCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::keyPressEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextEditCall5 call = reinterpret_cast<CuteQTextEditCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextEditCall6 call = reinterpret_cast<CuteQTextEditCall6>(taken[6]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::resizeEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextEditCall7 call = reinterpret_cast<CuteQTextEditCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::paintEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextEditCall8 call = reinterpret_cast<CuteQTextEditCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mousePressEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextEditCall9 call = reinterpret_cast<CuteQTextEditCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTextEditCall10 call = reinterpret_cast<CuteQTextEditCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
  void mouseDoubleClickEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTextEditCall11 call = reinterpret_cast<CuteQTextEditCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::mouseDoubleClickEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  bool QTextEdit::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTextEditCall12 call = reinterpret_cast<CuteQTextEditCall12>(taken[12]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QTextEdit::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(textedit)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(textedit)
  //  void QTextEdit::contextMenuEvent(QContextMenuEvent *e)
  void contextMenuEvent(QContextMenuEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTextEditCall13 call = reinterpret_cast<CuteQTextEditCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQTextEditCall14 call = reinterpret_cast<CuteQTextEditCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQTextEditCall15 call = reinterpret_cast<CuteQTextEditCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQTextEditCall16 call = reinterpret_cast<CuteQTextEditCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQTextEditCall17 call = reinterpret_cast<CuteQTextEditCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQTextEditCall18 call = reinterpret_cast<CuteQTextEditCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::focusInEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTextEditCall19 call = reinterpret_cast<CuteQTextEditCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTextEdit::focusOutEvent(e);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTextEditCall20 call = reinterpret_cast<CuteQTextEditCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTextEdit::showEvent(a0);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTextEditCall21 call = reinterpret_cast<CuteQTextEditCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQTextEditCall22 call = reinterpret_cast<CuteQTextEditCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQTextEditCall23 call = reinterpret_cast<CuteQTextEditCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QTextEdit::createMimeDataFromSelection();
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  bool QTextEdit::canInsertFromMimeData(const QMimeData *source) const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTextEditCall24 call = reinterpret_cast<CuteQTextEditCall24>(taken[24]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QTextEdit::canInsertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::insertFromMimeData(const QMimeData *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTextEditCall25 call = reinterpret_cast<CuteQTextEditCall25>(taken[25]);
      call(this, source, &handled);
      if (handled) return;
    }
    QTextEdit::insertFromMimeData(source);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
  //  void QTextEdit::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTextEditCall26 call = reinterpret_cast<CuteQTextEditCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQTextEditCall27 call = reinterpret_cast<CuteQTextEditCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQTextEditCall28 call = reinterpret_cast<CuteQTextEditCall28>(taken[28]);
      call(this, &cursor, &handled);
      if (handled) return;
    }
    QTextEdit::doSetTextCursor(cursor);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQTextEditCall29 call = reinterpret_cast<CuteQTextEditCall29>(taken[29]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQTextEditCall30 call = reinterpret_cast<CuteQTextEditCall30>(taken[30]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTextEditCall31 call = reinterpret_cast<CuteQTextEditCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQTextEditCall32 call = reinterpret_cast<CuteQTextEditCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQTextEditCall33 call = reinterpret_cast<CuteQTextEditCall33>(taken[33]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQTextEditCall34 call = reinterpret_cast<CuteQTextEditCall34>(taken[34]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQTextEditCall35 call = reinterpret_cast<CuteQTextEditCall35>(taken[35]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQTextEditCall36 call = reinterpret_cast<CuteQTextEditCall36>(taken[36]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTextEditCall37 call = reinterpret_cast<CuteQTextEditCall37>(taken[37]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQTextEditCall38 call = reinterpret_cast<CuteQTextEditCall38>(taken[38]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQTextEditCall39 call = reinterpret_cast<CuteQTextEditCall39>(taken[39]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQTextEditCall40 call = reinterpret_cast<CuteQTextEditCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQTextEditCall41 call = reinterpret_cast<CuteQTextEditCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTextEditCall42 call = reinterpret_cast<CuteQTextEditCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQTextEditCall43 call = reinterpret_cast<CuteQTextEditCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQTextEditCall44 call = reinterpret_cast<CuteQTextEditCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQTextEditCall45 call = reinterpret_cast<CuteQTextEditCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTextEditCall46 call = reinterpret_cast<CuteQTextEditCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTextEditCall47 call = reinterpret_cast<CuteQTextEditCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQTextEditCall48 call = reinterpret_cast<CuteQTextEditCall48>(taken[48]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[49]) {
      int handled = 0;
      CuteQTextEditCall49 call = reinterpret_cast<CuteQTextEditCall49>(taken[49]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[50]) {
      int handled = 0;
      CuteQTextEditCall50 call = reinterpret_cast<CuteQTextEditCall50>(taken[50]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[51]) {
      int handled = 0;
      CuteQTextEditCall51 call = reinterpret_cast<CuteQTextEditCall51>(taken[51]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQTextEditCall52 call = reinterpret_cast<CuteQTextEditCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQTextEditCall53 call = reinterpret_cast<CuteQTextEditCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      CuteQTextEditCall54 call = reinterpret_cast<CuteQTextEditCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[55]) {
      int handled = 0;
      CuteQTextEditCall55 call = reinterpret_cast<CuteQTextEditCall55>(taken[55]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTextEdit10metaObjectEv(
    const QTextEdit *self) {
  return self->metaObject();
}

//  void *QTextEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QTextEdit11qt_metacastEPKc(QTextEdit *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTextEdit::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QTextEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    QTextEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTextEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTextEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextEdit::tr(s, c, n));
}

//  QTextEditPrivate *QTextEdit::d_func()
extern "C" Q_DECL_EXPORT
QTextEditPrivate *ritual_ZN9QTextEdit6d_funcEv(QTextEdit *self) {
  return self->d_func();
}

//  const QTextEditPrivate *QTextEdit::d_func() const
extern "C" Q_DECL_EXPORT
const QTextEditPrivate *ritual_ZNK9QTextEdit6d_funcEv(
    const QTextEdit *self) {
  return self->d_func();
}

//  QTextEdit::QTextEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZN9QTextEditC1EP7QWidget(QWidget *parent) {
  return new CuteQTextEdit(parent);
}

//  QTextEdit::QTextEdit(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZN9QTextEditC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new CuteQTextEdit(*text, parent);
}

//  QTextEdit::~QTextEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEditD1Ev(QTextEdit *self) {
  delete self;
}

//  void QTextEdit::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11setDocumentEP13QTextDocument(
    QTextEdit *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QTextEdit::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK9QTextEdit8documentEv(const QTextEdit *self) {
  return self->document();
}

//  void QTextEdit::setPlaceholderText(const QString &placeholderText)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setPlaceholderTextERK7QString(
    QTextEdit *self,
    const QString *placeholderText) {
  self->setPlaceholderText(*placeholderText);
}

//  QString QTextEdit::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit15placeholderTextEv(const QTextEdit *self) {
  return new QString(self->placeholderText());
}

//  void QTextEdit::setTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setTextCursorERK11QTextCursor(
    QTextEdit *self,
    const QTextCursor *cursor) {
  self->setTextCursor(*cursor);
}

//  QTextCursor QTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK9QTextEdit10textCursorEv(const QTextEdit *self) {
  return new QTextCursor(self->textCursor());
}

//  bool QTextEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit10isReadOnlyEv(const QTextEdit *self) {
  return self->isReadOnly();
}

//  void QTextEdit::setReadOnly(bool ro)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11setReadOnlyEb(QTextEdit *self, bool ro) {
  self->setReadOnly(ro);
}

//  void QTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QTextEdit *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QTextEdit::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit20textInteractionFlagsEv(const QTextEdit *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  qreal QTextEdit::fontPointSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextEdit13fontPointSizeEv(const QTextEdit *self) {
  return self->fontPointSize();
}

//  QString QTextEdit::fontFamily() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit10fontFamilyEv(const QTextEdit *self) {
  return new QString(self->fontFamily());
}

//  int QTextEdit::fontWeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit10fontWeightEv(const QTextEdit *self) {
  return self->fontWeight();
}

//  bool QTextEdit::fontUnderline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit13fontUnderlineEv(const QTextEdit *self) {
  return self->fontUnderline();
}

//  bool QTextEdit::fontItalic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit10fontItalicEv(const QTextEdit *self) {
  return self->fontItalic();
}

//  QColor QTextEdit::textColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QTextEdit9textColorEv(const QTextEdit *self) {
  return new QColor(self->textColor());
}

//  QColor QTextEdit::textBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QTextEdit19textBackgroundColorEv(const QTextEdit *self) {
  return new QColor(self->textBackgroundColor());
}

//  QFont QTextEdit::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK9QTextEdit11currentFontEv(const QTextEdit *self) {
  return new QFont(self->currentFont());
}

//  Qt::Alignment QTextEdit::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit9alignmentEv(const QTextEdit *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QTextEdit::mergeCurrentCharFormat(const QTextCharFormat &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit22mergeCurrentCharFormatERK15QTextCharFormat(
    QTextEdit *self,
    const QTextCharFormat *modifier) {
  self->mergeCurrentCharFormat(*modifier);
}

//  void QTextEdit::setCurrentCharFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit20setCurrentCharFormatERK15QTextCharFormat(
    QTextEdit *self,
    const QTextCharFormat *format) {
  self->setCurrentCharFormat(*format);
}

//  QTextCharFormat QTextEdit::currentCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK9QTextEdit17currentCharFormatEv(
    const QTextEdit *self) {
  return new QTextCharFormat(self->currentCharFormat());
}

//  AutoFormatting QTextEdit::autoFormatting() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit14autoFormattingEv(const QTextEdit *self) {
  return static_cast<int>(self->autoFormatting().toInt());
}

//  void QTextEdit::setAutoFormatting(AutoFormatting features)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit17setAutoFormattingE6QFlagsINS_18AutoFormattingFlagEE(
    QTextEdit *self,
    int features) {
  self->setAutoFormatting(
      QFlags<QTextEdit::AutoFormattingFlag>::fromInt(features));
}

//  bool QTextEdit::tabChangesFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit15tabChangesFocusEv(const QTextEdit *self) {
  return self->tabChangesFocus();
}

//  void QTextEdit::setTabChangesFocus(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setTabChangesFocusEb(QTextEdit *self, bool b) {
  self->setTabChangesFocus(b);
}

//  void QTextEdit::setDocumentTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setDocumentTitleERK7QString(
    QTextEdit *self,
    const QString *title) {
  self->setDocumentTitle(*title);
}

//  QString QTextEdit::documentTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit13documentTitleEv(const QTextEdit *self) {
  return new QString(self->documentTitle());
}

//  bool QTextEdit::isUndoRedoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit17isUndoRedoEnabledEv(const QTextEdit *self) {
  return self->isUndoRedoEnabled();
}

//  void QTextEdit::setUndoRedoEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setUndoRedoEnabledEb(
    QTextEdit *self,
    bool enable) {
  self->setUndoRedoEnabled(enable);
}

//  LineWrapMode QTextEdit::lineWrapMode() const
extern "C" Q_DECL_EXPORT
QTextEdit::LineWrapMode ritual_ZNK9QTextEdit12lineWrapModeEv(
    const QTextEdit *self) {
  return self->lineWrapMode();
}

//  void QTextEdit::setLineWrapMode(LineWrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15setLineWrapModeENS_12LineWrapModeE(
    QTextEdit *self,
    QTextEdit::LineWrapMode mode) {
  self->setLineWrapMode(mode);
}

//  int QTextEdit::lineWrapColumnOrWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit21lineWrapColumnOrWidthEv(const QTextEdit *self) {
  return self->lineWrapColumnOrWidth();
}

//  void QTextEdit::setLineWrapColumnOrWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit24setLineWrapColumnOrWidthEi(
    QTextEdit *self,
    int w) {
  self->setLineWrapColumnOrWidth(w);
}

//  QTextOption::WrapMode QTextEdit::wordWrapMode() const
extern "C" Q_DECL_EXPORT
QTextOption::WrapMode ritual_ZNK9QTextEdit12wordWrapModeEv(
    const QTextEdit *self) {
  return self->wordWrapMode();
}

//  void QTextEdit::setWordWrapMode(QTextOption::WrapMode policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15setWordWrapModeEN11QTextOption8WrapModeE(
    QTextEdit *self,
    QTextOption::WrapMode policy) {
  self->setWordWrapMode(policy);
}

//  bool QTextEdit::find(const QString &exp, QTextDocument::FindFlags
//      options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTextEdit4findERK7QString6QFlagsIN13QTextDocument8FindFlagEE(
    QTextEdit *self,
    const QString *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

#if QT_CONFIG(regularexpression)
//  bool QTextEdit::find(const QRegularExpression &exp,
//      QTextDocument::FindFlags options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTextEdit4findERK18QRegularExpression6QFlagsIN13QTextDocument8FindFlagEE(
    QTextEdit *self,
    const QRegularExpression *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}
#endif  // QT_CONFIG(regularexpression)

//  QString QTextEdit::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit11toPlainTextEv(const QTextEdit *self) {
  return new QString(self->toPlainText());
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  QString QTextEdit::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit6toHtmlEv(const QTextEdit *self) {
  return new QString(self->toHtml());
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if QT_CONFIG(textmarkdownwriter)
//  QString QTextEdit::toMarkdown(QTextDocument::MarkdownFeatures features)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit10toMarkdownE6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    const QTextEdit *self,
    int features) {
  return new QString(
      self->toMarkdown(
          QFlags<QTextDocument::MarkdownFeature>::fromInt(features)));
}
#endif  // QT_CONFIG(textmarkdownwriter)

//  void QTextEdit::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit19ensureCursorVisibleEv(QTextEdit *self) {
  self->ensureCursorVisible();
}

//  QVariant QTextEdit::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN9QTextEdit12loadResourceEiRK4QUrl(
    QTextEdit *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

#if !defined(QT_NO_CONTEXTMENU)
//  QMenu *QTextEdit::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN9QTextEdit25createStandardContextMenuEv(QTextEdit *self) {
  return self->createStandardContextMenu();
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if !defined(QT_NO_CONTEXTMENU)
//  QMenu *QTextEdit::createStandardContextMenu(const QPoint &position)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN9QTextEdit25createStandardContextMenuERK6QPoint(
    QTextEdit *self,
    const QPoint *position) {
  return self->createStandardContextMenu(*position);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  QTextCursor QTextEdit::cursorForPosition(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK9QTextEdit17cursorForPositionERK6QPoint(
    const QTextEdit *self,
    const QPoint *pos) {
  return new QTextCursor(self->cursorForPosition(*pos));
}

//  QRect QTextEdit::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QTextEdit10cursorRectERK11QTextCursor(
    const QTextEdit *self,
    const QTextCursor *cursor) {
  return new QRect(self->cursorRect(*cursor));
}

//  QRect QTextEdit::cursorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QTextEdit10cursorRectEv(const QTextEdit *self) {
  return new QRect(self->cursorRect());
}

//  QString QTextEdit::anchorAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit8anchorAtERK6QPoint(
    const QTextEdit *self,
    const QPoint *pos) {
  return new QString(self->anchorAt(*pos));
}

//  bool QTextEdit::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit13overwriteModeEv(const QTextEdit *self) {
  return self->overwriteMode();
}

//  void QTextEdit::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setOverwriteModeEb(
    QTextEdit *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  qreal QTextEdit::tabStopDistance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextEdit15tabStopDistanceEv(const QTextEdit *self) {
  return self->tabStopDistance();
}

//  void QTextEdit::setTabStopDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setTabStopDistanceEd(
    QTextEdit *self,
    qreal distance) {
  self->setTabStopDistance(distance);
}

//  int QTextEdit::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit11cursorWidthEv(const QTextEdit *self) {
  return self->cursorWidth();
}

//  void QTextEdit::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14setCursorWidthEi(QTextEdit *self, int width) {
  self->setCursorWidth(width);
}

//  bool QTextEdit::acceptRichText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit14acceptRichTextEv(const QTextEdit *self) {
  return self->acceptRichText();
}

//  void QTextEdit::setAcceptRichText(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit17setAcceptRichTextEb(QTextEdit *self, bool accept) {
  self->setAcceptRichText(accept);
}

//  void QTextEdit::setExtraSelections(const QList<ExtraSelection>
//      &selections)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setExtraSelectionsERK5QListINS_14ExtraSelectionEE(
    QTextEdit *self,
    const QList<QTextEdit::ExtraSelection> *selections) {
  self->setExtraSelections(*selections);
}

//  QList<ExtraSelection> QTextEdit::extraSelections() const
extern "C" Q_DECL_EXPORT
QList<QTextEdit::ExtraSelection> *ritual_ZNK9QTextEdit15extraSelectionsEv(
    const QTextEdit *self) {
  return new QList<QTextEdit::ExtraSelection>(self->extraSelections());
}

//  void QTextEdit::moveCursor(QTextCursor::MoveOperation operation,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10moveCursorEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QTextEdit *self,
    QTextCursor::MoveOperation operation,
    QTextCursor::MoveMode mode) {
  self->moveCursor(operation, mode);
}

//  bool QTextEdit::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit8canPasteEv(const QTextEdit *self) {
  return self->canPaste();
}

//  void QTextEdit::print(QPagedPaintDevice *printer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QTextEdit5printEP17QPagedPaintDevice(
    const QTextEdit *self,
    QPagedPaintDevice *printer) {
  self->print(printer);
}

//  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}

//  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery query, QVariant
//      argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QTextEdit *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}

//  void QTextEdit::setFontPointSize(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setFontPointSizeEd(QTextEdit *self, qreal s) {
  self->setFontPointSize(s);
}

//  void QTextEdit::setFontFamily(const QString &fontFamily)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setFontFamilyERK7QString(
    QTextEdit *self,
    const QString *fontFamily) {
  self->setFontFamily(*fontFamily);
}

//  void QTextEdit::setFontWeight(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setFontWeightEi(QTextEdit *self, int w) {
  self->setFontWeight(w);
}

//  void QTextEdit::setFontUnderline(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setFontUnderlineEb(QTextEdit *self, bool b) {
  self->setFontUnderline(b);
}

//  void QTextEdit::setFontItalic(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setFontItalicEb(QTextEdit *self, bool b) {
  self->setFontItalic(b);
}

//  void QTextEdit::setTextColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12setTextColorERK6QColor(
    QTextEdit *self,
    const QColor *c) {
  self->setTextColor(*c);
}

//  void QTextEdit::setTextBackgroundColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit22setTextBackgroundColorERK6QColor(
    QTextEdit *self,
    const QColor *c) {
  self->setTextBackgroundColor(*c);
}

//  void QTextEdit::setCurrentFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14setCurrentFontERK5QFont(
    QTextEdit *self,
    const QFont *f) {
  self->setCurrentFont(*f);
}

//  void QTextEdit::setAlignment(Qt::Alignment a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTextEdit *self,
    int a) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a));
}

//  void QTextEdit::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12setPlainTextERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->setPlainText(*text);
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextEdit::setHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7setHtmlERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->setHtml(*text);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if QT_CONFIG(textmarkdownreader)
//  void QTextEdit::setMarkdown(const QString &markdown)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11setMarkdownERK7QString(
    QTextEdit *self,
    const QString *markdown) {
  self->setMarkdown(*markdown);
}
#endif  // QT_CONFIG(textmarkdownreader)

//  void QTextEdit::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7setTextERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->setText(*text);
}

#if !defined(QT_NO_CLIPBOARD)
//  void QTextEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit3cutEv(QTextEdit *self) {
  self->cut();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QTextEdit::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit4copyEv(QTextEdit *self) {
  self->copy();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QTextEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit5pasteEv(QTextEdit *self) {
  self->paste();
}
#endif  // !defined(QT_NO_CLIPBOARD)

//  void QTextEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit4undoEv(QTextEdit *self) {
  self->undo();
}

//  void QTextEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit4redoEv(QTextEdit *self) {
  self->redo();
}

//  void QTextEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit5clearEv(QTextEdit *self) {
  self->clear();
}

//  void QTextEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit9selectAllEv(QTextEdit *self) {
  self->selectAll();
}

//  void QTextEdit::insertPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15insertPlainTextERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->insertPlainText(*text);
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextEdit::insertHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10insertHtmlERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->insertHtml(*text);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  void QTextEdit::append(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit6appendERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->append(*text);
}

//  void QTextEdit::scrollToAnchor(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14scrollToAnchorERK7QString(
    QTextEdit *self,
    const QString *name) {
  self->scrollToAnchor(*name);
}

//  void QTextEdit::zoomIn(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit6zoomInEi(QTextEdit *self, int range) {
  self->zoomIn(range);
}

//  void QTextEdit::zoomOut(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7zoomOutEi(QTextEdit *self, int range) {
  self->zoomOut(range);
}

//  void QTextEdit::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11textChangedEv(QTextEdit *self) {
  self->textChanged();
}

//  void QTextEdit::undoAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13undoAvailableEb(QTextEdit *self, bool b) {
  self->undoAvailable(b);
}

//  void QTextEdit::redoAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13redoAvailableEb(QTextEdit *self, bool b) {
  self->redoAvailable(b);
}

//  void QTextEdit::currentCharFormatChanged(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit24currentCharFormatChangedERK15QTextCharFormat(
    QTextEdit *self,
    const QTextCharFormat *format) {
  self->currentCharFormatChanged(*format);
}

//  void QTextEdit::copyAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13copyAvailableEb(QTextEdit *self, bool b) {
  self->copyAvailable(b);
}

//  void QTextEdit::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16selectionChangedEv(QTextEdit *self) {
  self->selectionChanged();
}

//  void QTextEdit::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit21cursorPositionChangedEv(QTextEdit *self) {
  self->cursorPositionChanged();
}

//  bool QTextEdit::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTextEdit5eventEP6QEvent(QTextEdit *self, QEvent *e) {
  return self->event(e);
}

//  void QTextEdit::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10timerEventEP11QTimerEvent(
    QTextEdit *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QTextEdit::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13keyPressEventEP9QKeyEvent(
    QTextEdit *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  void QTextEdit::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15keyReleaseEventEP9QKeyEvent(
    QTextEdit *self,
    QKeyEvent *e) {
  self->keyReleaseEvent(e);
}

//  void QTextEdit::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11resizeEventEP12QResizeEvent(
    QTextEdit *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  void QTextEdit::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10paintEventEP11QPaintEvent(
    QTextEdit *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QTextEdit::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15mousePressEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QTextEdit::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14mouseMoveEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QTextEdit::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit17mouseReleaseEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

//  void QTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit21mouseDoubleClickEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  self->mouseDoubleClickEvent(e);
}

//  bool QTextEdit::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTextEdit18focusNextPrevChildEb(QTextEdit *self, bool next) {
  return self->focusNextPrevChild(next);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QTextEdit::contextMenuEvent(QContextMenuEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16contextMenuEventEP17QContextMenuEvent(
    QTextEdit *self,
    QContextMenuEvent *e) {
  self->contextMenuEvent(e);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14dragEnterEventEP15QDragEnterEvent(
    QTextEdit *self,
    QDragEnterEvent *e) {
  self->dragEnterEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14dragLeaveEventEP15QDragLeaveEvent(
    QTextEdit *self,
    QDragLeaveEvent *e) {
  self->dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13dragMoveEventEP14QDragMoveEvent(
    QTextEdit *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit9dropEventEP10QDropEvent(
    QTextEdit *self,
    QDropEvent *e) {
  self->dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

//  void QTextEdit::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12focusInEventEP11QFocusEvent(
    QTextEdit *self,
    QFocusEvent *e) {
  self->focusInEvent(e);
}

//  void QTextEdit::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13focusOutEventEP11QFocusEvent(
    QTextEdit *self,
    QFocusEvent *e) {
  self->focusOutEvent(e);
}

//  void QTextEdit::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit9showEventEP10QShowEvent(
    QTextEdit *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QTextEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11changeEventEP6QEvent(QTextEdit *self, QEvent *e) {
  self->changeEvent(e);
}

#if QT_CONFIG(wheelevent)
//  void QTextEdit::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10wheelEventEP11QWheelEvent(
    QTextEdit *self,
    QWheelEvent *e) {
  self->wheelEvent(e);
}
#endif  // QT_CONFIG(wheelevent)

//  QMimeData *QTextEdit::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK9QTextEdit27createMimeDataFromSelectionEv(
    const QTextEdit *self) {
  return self->createMimeDataFromSelection();
}

//  bool QTextEdit::canInsertFromMimeData(const QMimeData *source) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit21canInsertFromMimeDataEPK9QMimeData(
    const QTextEdit *self,
    const QMimeData *source) {
  return self->canInsertFromMimeData(source);
}

//  void QTextEdit::insertFromMimeData(const QMimeData *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18insertFromMimeDataEPK9QMimeData(
    QTextEdit *self,
    const QMimeData *source) {
  self->insertFromMimeData(source);
}

//  void QTextEdit::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16inputMethodEventEP17QInputMethodEvent(
    QTextEdit *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}

//  QTextEdit::QTextEdit(QTextEditPrivate &dd, QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZN9QTextEditC1ER16QTextEditPrivateP7QWidget(
    QTextEditPrivate *dd,
    QWidget *parent) {
  return new CuteQTextEdit(*dd, parent);
}

//  void QTextEdit::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16scrollContentsByEii(
    QTextEdit *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QTextEdit::doSetTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15doSetTextCursorERK11QTextCursor(
    QTextEdit *self,
    const QTextCursor *cursor) {
  self->doSetTextCursor(*cursor);
}

//  void QTextEdit::zoomInF(float range)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7zoomInFEf(QTextEdit *self, float range) {
  self->zoomInF(range);
}

//  a Python function taken by a CuteQTextEdit, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextEdit(QTextEdit *self, const char *key, void *call) {
  return static_cast<CuteQTextEdit *>(self)->take(key, call);
}

//  QVariant QTextEdit::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN9QTextEdit12loadResourceEiRK4QUrl(
    QTextEdit *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->QTextEdit::loadResource(type, *name));
}

//  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->QTextEdit::inputMethodQuery(property));
}

//  bool QTextEdit::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QTextEdit5eventEP6QEvent(QTextEdit *self, QEvent *e) {
  return static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::event(e);
}

//  void QTextEdit::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit10timerEventEP11QTimerEvent(
    QTextEdit *self,
    QTimerEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::timerEvent(e);
}

//  void QTextEdit::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit13keyPressEventEP9QKeyEvent(
    QTextEdit *self,
    QKeyEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::keyPressEvent(e);
}

//  void QTextEdit::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit15keyReleaseEventEP9QKeyEvent(
    QTextEdit *self,
    QKeyEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::keyReleaseEvent(e);
}

//  void QTextEdit::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit11resizeEventEP12QResizeEvent(
    QTextEdit *self,
    QResizeEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::resizeEvent(e);
}

//  void QTextEdit::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit10paintEventEP11QPaintEvent(
    QTextEdit *self,
    QPaintEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::paintEvent(e);
}

//  void QTextEdit::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit15mousePressEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::mousePressEvent(e);
}

//  void QTextEdit::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit14mouseMoveEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::mouseMoveEvent(e);
}

//  void QTextEdit::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit17mouseReleaseEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::mouseReleaseEvent(e);
}

//  void QTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit21mouseDoubleClickEventEP11QMouseEvent(
    QTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::mouseDoubleClickEvent(e);
}

//  bool QTextEdit::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QTextEdit18focusNextPrevChildEb(
    QTextEdit *self,
    bool next) {
  return static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::focusNextPrevChild(
      next);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QTextEdit::contextMenuEvent(QContextMenuEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit16contextMenuEventEP17QContextMenuEvent(
    QTextEdit *self,
    QContextMenuEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::contextMenuEvent(e);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit14dragEnterEventEP15QDragEnterEvent(
    QTextEdit *self,
    QDragEnterEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::dragEnterEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit14dragLeaveEventEP15QDragLeaveEvent(
    QTextEdit *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit13dragMoveEventEP14QDragMoveEvent(
    QTextEdit *self,
    QDragMoveEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTextEdit::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit9dropEventEP10QDropEvent(
    QTextEdit *self,
    QDropEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

//  void QTextEdit::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit12focusInEventEP11QFocusEvent(
    QTextEdit *self,
    QFocusEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::focusInEvent(e);
}

//  void QTextEdit::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit13focusOutEventEP11QFocusEvent(
    QTextEdit *self,
    QFocusEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::focusOutEvent(e);
}

//  void QTextEdit::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit9showEventEP10QShowEvent(
    QTextEdit *self,
    QShowEvent *a0) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::showEvent(a0);
}

//  void QTextEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit11changeEventEP6QEvent(
    QTextEdit *self,
    QEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::changeEvent(e);
}

#if QT_CONFIG(wheelevent)
//  void QTextEdit::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit10wheelEventEP11QWheelEvent(
    QTextEdit *self,
    QWheelEvent *e) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::wheelEvent(e);
}
#endif  // QT_CONFIG(wheelevent)

//  QMimeData *QTextEdit::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_own_ZNK9QTextEdit27createMimeDataFromSelectionEv(
    const QTextEdit *self) {
  return static_cast<const OwnQTextEdit *>(self)->OwnQTextEdit::createMimeDataFromSelection();
}

//  bool QTextEdit::canInsertFromMimeData(const QMimeData *source) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QTextEdit21canInsertFromMimeDataEPK9QMimeData(
    const QTextEdit *self,
    const QMimeData *source) {
  return static_cast<const OwnQTextEdit *>(self)->OwnQTextEdit::canInsertFromMimeData(
      source);
}

//  void QTextEdit::insertFromMimeData(const QMimeData *source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit18insertFromMimeDataEPK9QMimeData(
    QTextEdit *self,
    const QMimeData *source) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::insertFromMimeData(
      source);
}

//  void QTextEdit::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit16inputMethodEventEP17QInputMethodEvent(
    QTextEdit *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::inputMethodEvent(a0);
}

//  void QTextEdit::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit16scrollContentsByEii(
    QTextEdit *self,
    int dx,
    int dy) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::scrollContentsBy(dx, dy);
}

//  void QTextEdit::doSetTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTextEdit15doSetTextCursorERK11QTextCursor(
    QTextEdit *self,
    const QTextCursor *cursor) {
  static_cast<OwnQTextEdit *>(self)->OwnQTextEdit::doSetTextCursor(*cursor);
}

//  a QList<QTextEdit::ExtraSelection> a ritual of QTextEdit gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextEdit__QList_QTextEdit_ExtraSelection(
    QList<QTextEdit::ExtraSelection> *self) {
  delete self;
}

#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(textedit)
