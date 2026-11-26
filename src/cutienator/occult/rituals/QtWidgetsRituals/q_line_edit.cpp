//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlineedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmargins.h>
#include <QtGui/qicon.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLineEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLineEdit : QLineEdit {
  using QLineEdit::mousePressEvent;
  using QLineEdit::mouseMoveEvent;
  using QLineEdit::mouseReleaseEvent;
  using QLineEdit::mouseDoubleClickEvent;
  using QLineEdit::keyPressEvent;
  using QLineEdit::keyReleaseEvent;
  using QLineEdit::focusInEvent;
  using QLineEdit::focusOutEvent;
  using QLineEdit::paintEvent;
  using QLineEdit::dragEnterEvent;
  using QLineEdit::dragMoveEvent;
  using QLineEdit::dragLeaveEvent;
  using QLineEdit::dropEvent;
  using QLineEdit::changeEvent;
  using QLineEdit::contextMenuEvent;
  using QLineEdit::inputMethodEvent;
  using QLineEdit::initStyleOption;
};

//  A QLineEdit that Python can take functions over in. Every QLineEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(lineedit)
typedef const QSize * (*CuteQLineEditCall0)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef const QSize * (*CuteQLineEditCall1)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall2)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall6)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall7)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall8)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall9)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall10)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall11)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall12)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall13)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall14)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall16)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall18)(const void *, QStyleOptionFrame *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef const QVariant * (*CuteQLineEditCall19)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef void (*CuteQLineEditCall20)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef bool (*CuteQLineEditCall21)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQLineEditCall22)(const void *, int *);
typedef void (*CuteQLineEditCall23)(const void *, bool, int *);
typedef int (*CuteQLineEditCall24)(const void *, int, int *);
typedef bool (*CuteQLineEditCall25)(const void *, int *);
typedef void * (*CuteQLineEditCall26)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQLineEditCall27)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQLineEditCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQLineEditCall29)(const void *, QEvent *, int *);
typedef void (*CuteQLineEditCall30)(const void *, QMoveEvent *, int *);
typedef void (*CuteQLineEditCall31)(const void *, QResizeEvent *, int *);
typedef void (*CuteQLineEditCall32)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQLineEditCall33)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQLineEditCall34)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQLineEditCall35)(const void *, QShowEvent *, int *);
typedef void (*CuteQLineEditCall36)(const void *, QHideEvent *, int *);
typedef int (*CuteQLineEditCall37)(const void *, int, int *);
typedef void (*CuteQLineEditCall38)(const void *, QPainter *, int *);
typedef void * (*CuteQLineEditCall39)(const void *, QPoint *, int *);
typedef void * (*CuteQLineEditCall40)(const void *, int *);
typedef bool (*CuteQLineEditCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLineEditCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineEditCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineEditCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineEditCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineEditCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLineEdit : public QLineEdit {
public:
  using QLineEdit::QLineEdit;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK9QLineEdit15initStyleOptionEP17QStyleOptionFrame")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[32] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(lineedit)
  //  QSize QLineEdit::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLineEditCall0 call = reinterpret_cast<CuteQLineEditCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLineEdit::sizeHint();
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  QSize QLineEdit::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLineEditCall1 call = reinterpret_cast<CuteQLineEditCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLineEdit::minimumSizeHint();
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLineEditCall2 call = reinterpret_cast<CuteQLineEditCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLineEditCall3 call = reinterpret_cast<CuteQLineEditCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLineEditCall4 call = reinterpret_cast<CuteQLineEditCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLineEditCall5 call = reinterpret_cast<CuteQLineEditCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseDoubleClickEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLineEditCall6 call = reinterpret_cast<CuteQLineEditCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLineEditCall7 call = reinterpret_cast<CuteQLineEditCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::keyReleaseEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLineEditCall8 call = reinterpret_cast<CuteQLineEditCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::focusInEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLineEditCall9 call = reinterpret_cast<CuteQLineEditCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::focusOutEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLineEditCall10 call = reinterpret_cast<CuteQLineEditCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::paintEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLineEditCall11 call = reinterpret_cast<CuteQLineEditCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLineEditCall12 call = reinterpret_cast<CuteQLineEditCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLineEdit::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLineEditCall13 call = reinterpret_cast<CuteQLineEditCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLineEdit::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLineEditCall14 call = reinterpret_cast<CuteQLineEditCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::dropEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLineEditCall15 call = reinterpret_cast<CuteQLineEditCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::changeEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLineEditCall16 call = reinterpret_cast<CuteQLineEditCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLineEditCall17 call = reinterpret_cast<CuteQLineEditCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQLineEditCall18 call = reinterpret_cast<CuteQLineEditCall18>(taken[18]);
      call(this, option, &handled);
      if (handled) return;
    }
    QLineEdit::initStyleOption(option);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQLineEditCall19 call = reinterpret_cast<CuteQLineEditCall19>(taken[19]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QLineEdit::inputMethodQuery(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLineEditCall20 call = reinterpret_cast<CuteQLineEditCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::timerEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
  //  bool QLineEdit::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLineEditCall21 call = reinterpret_cast<CuteQLineEditCall21>(taken[21]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLineEdit::event(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQLineEditCall22 call = reinterpret_cast<CuteQLineEditCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLineEditCall23 call = reinterpret_cast<CuteQLineEditCall23>(taken[23]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQLineEditCall24 call = reinterpret_cast<CuteQLineEditCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQLineEditCall25 call = reinterpret_cast<CuteQLineEditCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQLineEditCall26 call = reinterpret_cast<CuteQLineEditCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQLineEditCall27 call = reinterpret_cast<CuteQLineEditCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQLineEditCall28 call = reinterpret_cast<CuteQLineEditCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQLineEditCall29 call = reinterpret_cast<CuteQLineEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQLineEditCall30 call = reinterpret_cast<CuteQLineEditCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQLineEditCall31 call = reinterpret_cast<CuteQLineEditCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQLineEditCall32 call = reinterpret_cast<CuteQLineEditCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQLineEditCall33 call = reinterpret_cast<CuteQLineEditCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQLineEditCall34 call = reinterpret_cast<CuteQLineEditCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQLineEditCall35 call = reinterpret_cast<CuteQLineEditCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQLineEditCall36 call = reinterpret_cast<CuteQLineEditCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQLineEditCall37 call = reinterpret_cast<CuteQLineEditCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQLineEditCall38 call = reinterpret_cast<CuteQLineEditCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQLineEditCall39 call = reinterpret_cast<CuteQLineEditCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQLineEditCall40 call = reinterpret_cast<CuteQLineEditCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQLineEditCall41 call = reinterpret_cast<CuteQLineEditCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQLineEditCall42 call = reinterpret_cast<CuteQLineEditCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQLineEditCall43 call = reinterpret_cast<CuteQLineEditCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQLineEditCall44 call = reinterpret_cast<CuteQLineEditCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQLineEditCall45 call = reinterpret_cast<CuteQLineEditCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQLineEditCall46 call = reinterpret_cast<CuteQLineEditCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLineEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QLineEdit10metaObjectEv(
    const QLineEdit *self) {
  return self->metaObject();
}

//  void *QLineEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QLineEdit11qt_metacastEPKc(QLineEdit *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLineEdit::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QLineEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    QLineEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLineEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QLineEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLineEdit::tr(s, c, n));
}

//  QLineEdit::QLineEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZN9QLineEditC1EP7QWidget(QWidget *parent) {
  return new CuteQLineEdit(parent);
}

//  QLineEdit::QLineEdit(const QString &a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZN9QLineEditC1ERK7QStringP7QWidget(
    const QString *a0,
    QWidget *parent) {
  return new CuteQLineEdit(*a0, parent);
}

//  QLineEdit::~QLineEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEditD1Ev(QLineEdit *self) {
  delete self;
}

//  QString QLineEdit::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit4textEv(const QLineEdit *self) {
  return new QString(self->text());
}

//  QString QLineEdit::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit11displayTextEv(const QLineEdit *self) {
  return new QString(self->displayText());
}

//  QString QLineEdit::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit15placeholderTextEv(const QLineEdit *self) {
  return new QString(self->placeholderText());
}

//  void QLineEdit::setPlaceholderText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit18setPlaceholderTextERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->setPlaceholderText(*a0);
}

//  int QLineEdit::maxLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit9maxLengthEv(const QLineEdit *self) {
  return self->maxLength();
}

//  void QLineEdit::setMaxLength(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setMaxLengthEi(QLineEdit *self, int a0) {
  self->setMaxLength(a0);
}

//  void QLineEdit::setFrame(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit8setFrameEb(QLineEdit *self, bool a0) {
  self->setFrame(a0);
}

//  bool QLineEdit::hasFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit8hasFrameEv(const QLineEdit *self) {
  return self->hasFrame();
}

//  void QLineEdit::setClearButtonEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit21setClearButtonEnabledEb(
    QLineEdit *self,
    bool enable) {
  self->setClearButtonEnabled(enable);
}

//  bool QLineEdit::isClearButtonEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit20isClearButtonEnabledEv(const QLineEdit *self) {
  return self->isClearButtonEnabled();
}

//  EchoMode QLineEdit::echoMode() const
extern "C" Q_DECL_EXPORT
QLineEdit::EchoMode ritual_ZNK9QLineEdit8echoModeEv(const QLineEdit *self) {
  return self->echoMode();
}

//  void QLineEdit::setEchoMode(EchoMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11setEchoModeENS_8EchoModeE(
    QLineEdit *self,
    QLineEdit::EchoMode a0) {
  self->setEchoMode(a0);
}

//  bool QLineEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit10isReadOnlyEv(const QLineEdit *self) {
  return self->isReadOnly();
}

//  void QLineEdit::setReadOnly(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11setReadOnlyEb(QLineEdit *self, bool a0) {
  self->setReadOnly(a0);
}

#if !defined(QT_NO_VALIDATOR)
//  void QLineEdit::setValidator(const QValidator *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setValidatorEPK10QValidator(
    QLineEdit *self,
    const QValidator *a0) {
  self->setValidator(a0);
}
#endif  // !defined(QT_NO_VALIDATOR)

#if !defined(QT_NO_VALIDATOR)
//  const QValidator *QLineEdit::validator() const
extern "C" Q_DECL_EXPORT
const QValidator *ritual_ZNK9QLineEdit9validatorEv(const QLineEdit *self) {
  return self->validator();
}
#endif  // !defined(QT_NO_VALIDATOR)

#if QT_CONFIG(completer)
//  void QLineEdit::setCompleter(QCompleter *completer)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setCompleterEP10QCompleter(
    QLineEdit *self,
    QCompleter *completer) {
  self->setCompleter(completer);
}
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
//  QCompleter *QLineEdit::completer() const
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZNK9QLineEdit9completerEv(const QLineEdit *self) {
  return self->completer();
}
#endif  // QT_CONFIG(completer)

//  QSize QLineEdit::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QLineEdit8sizeHintEv(const QLineEdit *self) {
  return new QSize(self->sizeHint());
}

//  QSize QLineEdit::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QLineEdit15minimumSizeHintEv(const QLineEdit *self) {
  return new QSize(self->minimumSizeHint());
}

//  int QLineEdit::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit14cursorPositionEv(const QLineEdit *self) {
  return self->cursorPosition();
}

//  void QLineEdit::setCursorPosition(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit17setCursorPositionEi(QLineEdit *self, int a0) {
  self->setCursorPosition(a0);
}

//  int QLineEdit::cursorPositionAt(const QPoint &pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QLineEdit16cursorPositionAtERK6QPoint(
    QLineEdit *self,
    const QPoint *pos) {
  return self->cursorPositionAt(*pos);
}

//  void QLineEdit::setAlignment(Qt::Alignment flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLineEdit *self,
    int flag) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(flag));
}

//  Qt::Alignment QLineEdit::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit9alignmentEv(const QLineEdit *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLineEdit::cursorForward(bool mark, int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13cursorForwardEbi(
    QLineEdit *self,
    bool mark,
    int steps) {
  self->cursorForward(mark, steps);
}

//  void QLineEdit::cursorBackward(bool mark, int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14cursorBackwardEbi(
    QLineEdit *self,
    bool mark,
    int steps) {
  self->cursorBackward(mark, steps);
}

//  void QLineEdit::cursorWordForward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit17cursorWordForwardEb(QLineEdit *self, bool mark) {
  self->cursorWordForward(mark);
}

//  void QLineEdit::cursorWordBackward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit18cursorWordBackwardEb(QLineEdit *self, bool mark) {
  self->cursorWordBackward(mark);
}

//  void QLineEdit::backspace()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9backspaceEv(QLineEdit *self) {
  self->backspace();
}

//  void QLineEdit::del()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit3delEv(QLineEdit *self) {
  self->del();
}

//  void QLineEdit::home(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit4homeEb(QLineEdit *self, bool mark) {
  self->home(mark);
}

//  void QLineEdit::end(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit3endEb(QLineEdit *self, bool mark) {
  self->end(mark);
}

//  bool QLineEdit::isModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit10isModifiedEv(const QLineEdit *self) {
  return self->isModified();
}

//  void QLineEdit::setModified(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11setModifiedEb(QLineEdit *self, bool a0) {
  self->setModified(a0);
}

//  void QLineEdit::setSelection(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setSelectionEii(QLineEdit *self, int a0, int a1) {
  self->setSelection(a0, a1);
}

//  bool QLineEdit::hasSelectedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit15hasSelectedTextEv(const QLineEdit *self) {
  return self->hasSelectedText();
}

//  QString QLineEdit::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit12selectedTextEv(const QLineEdit *self) {
  return new QString(self->selectedText());
}

//  int QLineEdit::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit14selectionStartEv(const QLineEdit *self) {
  return self->selectionStart();
}

//  int QLineEdit::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit12selectionEndEv(const QLineEdit *self) {
  return self->selectionEnd();
}

//  int QLineEdit::selectionLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit15selectionLengthEv(const QLineEdit *self) {
  return self->selectionLength();
}

//  bool QLineEdit::isUndoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit15isUndoAvailableEv(const QLineEdit *self) {
  return self->isUndoAvailable();
}

//  bool QLineEdit::isRedoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit15isRedoAvailableEv(const QLineEdit *self) {
  return self->isRedoAvailable();
}

//  void QLineEdit::setDragEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14setDragEnabledEb(QLineEdit *self, bool b) {
  self->setDragEnabled(b);
}

//  bool QLineEdit::dragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit11dragEnabledEv(const QLineEdit *self) {
  return self->dragEnabled();
}

//  void QLineEdit::setCursorMoveStyle(Qt::CursorMoveStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit18setCursorMoveStyleEN2Qt15CursorMoveStyleE(
    QLineEdit *self,
    Qt::CursorMoveStyle style) {
  self->setCursorMoveStyle(style);
}

//  Qt::CursorMoveStyle QLineEdit::cursorMoveStyle() const
extern "C" Q_DECL_EXPORT
Qt::CursorMoveStyle ritual_ZNK9QLineEdit15cursorMoveStyleEv(
    const QLineEdit *self) {
  return self->cursorMoveStyle();
}

//  QString QLineEdit::inputMask() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit9inputMaskEv(const QLineEdit *self) {
  return new QString(self->inputMask());
}

//  void QLineEdit::setInputMask(const QString &inputMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setInputMaskERK7QString(
    QLineEdit *self,
    const QString *inputMask) {
  self->setInputMask(*inputMask);
}

//  bool QLineEdit::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit18hasAcceptableInputEv(const QLineEdit *self) {
  return self->hasAcceptableInput();
}

//  void QLineEdit::setTextMargins(int left, int top, int right, int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14setTextMarginsEiiii(
    QLineEdit *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setTextMargins(left, top, right, bottom);
}

//  void QLineEdit::setTextMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14setTextMarginsERK8QMargins(
    QLineEdit *self,
    const QMargins *margins) {
  self->setTextMargins(*margins);
}

//  QMargins QLineEdit::textMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK9QLineEdit11textMarginsEv(const QLineEdit *self) {
  return new QMargins(self->textMargins());
}

#if QT_CONFIG(action)
//  void QLineEdit::addAction(QAction *action, ActionPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9addActionEP7QActionNS_14ActionPositionE(
    QLineEdit *self,
    QAction *action,
    QLineEdit::ActionPosition position) {
  self->addAction(action, position);
}
#endif  // QT_CONFIG(action)

#if QT_CONFIG(action)
//  QAction *QLineEdit::addAction(const QIcon &icon, ActionPosition position)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN9QLineEdit9addActionERK5QIconNS_14ActionPositionE(
    QLineEdit *self,
    const QIcon *icon,
    QLineEdit::ActionPosition position) {
  return self->addAction(*icon, position);
}
#endif  // QT_CONFIG(action)

//  void QLineEdit::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit7setTextERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->setText(*a0);
}

//  void QLineEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit5clearEv(QLineEdit *self) {
  self->clear();
}

//  void QLineEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9selectAllEv(QLineEdit *self) {
  self->selectAll();
}

//  void QLineEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit4undoEv(QLineEdit *self) {
  self->undo();
}

//  void QLineEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit4redoEv(QLineEdit *self) {
  self->redo();
}

#if !defined(QT_NO_CLIPBOARD)
//  void QLineEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit3cutEv(QLineEdit *self) {
  self->cut();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QLineEdit::copy() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QLineEdit4copyEv(const QLineEdit *self) {
  self->copy();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QLineEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit5pasteEv(QLineEdit *self) {
  self->paste();
}
#endif  // !defined(QT_NO_CLIPBOARD)

//  void QLineEdit::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit8deselectEv(QLineEdit *self) {
  self->deselect();
}

//  void QLineEdit::insert(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit6insertERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->insert(*a0);
}

#if !defined(QT_NO_CONTEXTMENU)
//  QMenu *QLineEdit::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN9QLineEdit25createStandardContextMenuEv(QLineEdit *self) {
  return self->createStandardContextMenu();
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QLineEdit::textChanged(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11textChangedERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->textChanged(*a0);
}

//  void QLineEdit::textEdited(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit10textEditedERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->textEdited(*a0);
}

//  void QLineEdit::cursorPositionChanged(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit21cursorPositionChangedEii(
    QLineEdit *self,
    int a0,
    int a1) {
  self->cursorPositionChanged(a0, a1);
}

//  void QLineEdit::returnPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13returnPressedEv(QLineEdit *self) {
  self->returnPressed();
}

//  void QLineEdit::editingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit15editingFinishedEv(QLineEdit *self) {
  self->editingFinished();
}

//  void QLineEdit::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit16selectionChangedEv(QLineEdit *self) {
  self->selectionChanged();
}

//  void QLineEdit::inputRejected()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13inputRejectedEv(QLineEdit *self) {
  self->inputRejected();
}

//  void QLineEdit::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit15mousePressEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QLineEdit::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14mouseMoveEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QLineEdit::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit17mouseReleaseEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QLineEdit::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit21mouseDoubleClickEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  self->mouseDoubleClickEvent(a0);
}

//  void QLineEdit::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13keyPressEventEP9QKeyEvent(
    QLineEdit *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QLineEdit::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit15keyReleaseEventEP9QKeyEvent(
    QLineEdit *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QLineEdit::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12focusInEventEP11QFocusEvent(
    QLineEdit *self,
    QFocusEvent *a0) {
  self->focusInEvent(a0);
}

//  void QLineEdit::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13focusOutEventEP11QFocusEvent(
    QLineEdit *self,
    QFocusEvent *a0) {
  self->focusOutEvent(a0);
}

//  void QLineEdit::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit10paintEventEP11QPaintEvent(
    QLineEdit *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14dragEnterEventEP15QDragEnterEvent(
    QLineEdit *self,
    QDragEnterEvent *a0) {
  self->dragEnterEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13dragMoveEventEP14QDragMoveEvent(
    QLineEdit *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14dragLeaveEventEP15QDragLeaveEvent(
    QLineEdit *self,
    QDragLeaveEvent *e) {
  self->dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9dropEventEP10QDropEvent(
    QLineEdit *self,
    QDropEvent *a0) {
  self->dropEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QLineEdit::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11changeEventEP6QEvent(QLineEdit *self, QEvent *a0) {
  self->changeEvent(a0);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QLineEdit::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit16contextMenuEventEP17QContextMenuEvent(
    QLineEdit *self,
    QContextMenuEvent *a0) {
  self->contextMenuEvent(a0);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QLineEdit::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit16inputMethodEventEP17QInputMethodEvent(
    QLineEdit *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}

//  void QLineEdit::initStyleOption(QStyleOptionFrame *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QLineEdit15initStyleOptionEP17QStyleOptionFrame(
    const QLineEdit *self,
    QStyleOptionFrame *option) {
  self->initStyleOption(option);
}

//  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QLineEdit *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery property,
//      QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QLineEdit *self,
    Qt::InputMethodQuery property,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(property, *argument));
}

//  void QLineEdit::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit10timerEventEP11QTimerEvent(
    QLineEdit *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  bool QLineEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QLineEdit5eventEP6QEvent(QLineEdit *self, QEvent *a0) {
  return self->event(a0);
}

//  QRect QLineEdit::cursorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QLineEdit10cursorRectEv(const QLineEdit *self) {
  return new QRect(self->cursorRect());
}

//  QLineEditPrivate *QLineEdit::d_func()
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZN9QLineEdit6d_funcEv(QLineEdit *self) {
  return self->d_func();
}

//  const QLineEditPrivate *QLineEdit::d_func() const
extern "C" Q_DECL_EXPORT
const QLineEditPrivate *ritual_ZNK9QLineEdit6d_funcEv(
    const QLineEdit *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLineEdit, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLineEdit(QLineEdit *self, const char *key, void *call) {
  return static_cast<CuteQLineEdit *>(self)->take(key, call);
}

//  QSize QLineEdit::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QLineEdit8sizeHintEv(const QLineEdit *self) {
  return new QSize(self->QLineEdit::sizeHint());
}

//  QSize QLineEdit::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QLineEdit15minimumSizeHintEv(const QLineEdit *self) {
  return new QSize(self->QLineEdit::minimumSizeHint());
}

//  void QLineEdit::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit15mousePressEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::mousePressEvent(a0);
}

//  void QLineEdit::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit14mouseMoveEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::mouseMoveEvent(a0);
}

//  void QLineEdit::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit17mouseReleaseEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::mouseReleaseEvent(a0);
}

//  void QLineEdit::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit21mouseDoubleClickEventEP11QMouseEvent(
    QLineEdit *self,
    QMouseEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::mouseDoubleClickEvent(a0);
}

//  void QLineEdit::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit13keyPressEventEP9QKeyEvent(
    QLineEdit *self,
    QKeyEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::keyPressEvent(a0);
}

//  void QLineEdit::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit15keyReleaseEventEP9QKeyEvent(
    QLineEdit *self,
    QKeyEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::keyReleaseEvent(a0);
}

//  void QLineEdit::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit12focusInEventEP11QFocusEvent(
    QLineEdit *self,
    QFocusEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::focusInEvent(a0);
}

//  void QLineEdit::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit13focusOutEventEP11QFocusEvent(
    QLineEdit *self,
    QFocusEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::focusOutEvent(a0);
}

//  void QLineEdit::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit10paintEventEP11QPaintEvent(
    QLineEdit *self,
    QPaintEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::paintEvent(a0);
}

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit14dragEnterEventEP15QDragEnterEvent(
    QLineEdit *self,
    QDragEnterEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::dragEnterEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit13dragMoveEventEP14QDragMoveEvent(
    QLineEdit *self,
    QDragMoveEvent *e) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit14dragLeaveEventEP15QDragLeaveEvent(
    QLineEdit *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QLineEdit::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit9dropEventEP10QDropEvent(
    QLineEdit *self,
    QDropEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::dropEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QLineEdit::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit11changeEventEP6QEvent(
    QLineEdit *self,
    QEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::changeEvent(a0);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QLineEdit::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit16contextMenuEventEP17QContextMenuEvent(
    QLineEdit *self,
    QContextMenuEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::contextMenuEvent(a0);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QLineEdit::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit16inputMethodEventEP17QInputMethodEvent(
    QLineEdit *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQLineEdit *>(self)->OwnQLineEdit::inputMethodEvent(a0);
}

//  void QLineEdit::initStyleOption(QStyleOptionFrame *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QLineEdit15initStyleOptionEP17QStyleOptionFrame(
    const QLineEdit *self,
    QStyleOptionFrame *option) {
  static_cast<const OwnQLineEdit *>(self)->OwnQLineEdit::initStyleOption(
      option);
}

//  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QLineEdit *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->QLineEdit::inputMethodQuery(a0));
}

//  void QLineEdit::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QLineEdit10timerEventEP11QTimerEvent(
    QLineEdit *self,
    QTimerEvent *a0) {
  self->QLineEdit::timerEvent(a0);
}

//  bool QLineEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QLineEdit5eventEP6QEvent(QLineEdit *self, QEvent *a0) {
  return self->QLineEdit::event(a0);
}

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(lineedit)
