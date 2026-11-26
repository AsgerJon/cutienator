//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(action)
#include <QtGui/qaction.h>
#endif
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QDesignerMenuBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDesignerMenuBar : QDesignerMenuBar {
  using QDesignerMenuBar::actionEvent;
  using QDesignerMenuBar::dragEnterEvent;
  using QDesignerMenuBar::dragMoveEvent;
  using QDesignerMenuBar::dragLeaveEvent;
  using QDesignerMenuBar::dropEvent;
  using QDesignerMenuBar::paintEvent;
  using QDesignerMenuBar::focusOutEvent;
  using QDesignerMenuBar::keyPressEvent;
  using QDesignerMenuBar::keyReleaseEvent;
};

//  A QDesignerMenuBar that Python can take functions over in. Every QDesignerMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerMenuBarCall0)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuBarCall1)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuBarCall2)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuBarCall3)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuBarCall4)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuBarCall5)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerMenuBarCall6)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerMenuBarCall7)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerMenuBarCall8)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(menubar)
typedef const QSize * (*CuteQDesignerMenuBarCall9)(const void *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef const QSize * (*CuteQDesignerMenuBarCall10)(const void *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef int (*CuteQDesignerMenuBarCall11)(const void *, int, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall12)(const void *, bool, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall13)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall15)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall16)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall18)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(menubar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall20)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
typedef bool (*CuteQDesignerMenuBarCall21)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
typedef bool (*CuteQDesignerMenuBarCall22)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
typedef void (*CuteQDesignerMenuBarCall23)(const void *, QStyleOptionMenuItem *, const QAction *, int *);
#endif  // QT_CONFIG(menubar)
typedef int (*CuteQDesignerMenuBarCall24)(const void *, int *);
typedef bool (*CuteQDesignerMenuBarCall25)(const void *, int *);
typedef void * (*CuteQDesignerMenuBarCall26)(const void *, int *);
typedef void (*CuteQDesignerMenuBarCall27)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerMenuBarCall28)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerMenuBarCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerMenuBarCall30)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerMenuBarCall31)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerMenuBarCall32)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerMenuBarCall33)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerMenuBarCall34)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerMenuBarCall35)(const void *, QHideEvent *, int *);
typedef int (*CuteQDesignerMenuBarCall36)(const void *, int, int *);
typedef void (*CuteQDesignerMenuBarCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerMenuBarCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerMenuBarCall39)(const void *, int *);
typedef void (*CuteQDesignerMenuBarCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerMenuBarCall41)(const void *, int, int *);
typedef bool (*CuteQDesignerMenuBarCall42)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuBarCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuBarCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuBarCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuBarCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerMenuBar : public QDesignerMenuBar {
public:
  using QDesignerMenuBar::QDesignerMenuBar;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK8QMenuBar15initStyleOptionEP20QStyleOptionMenuItemPK7QAction")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
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
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[31] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[42] = call;
      return true;
    }
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

#if !defined(QT_NO_ACTION)
  //  void QDesignerMenuBar::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMenuBarCall0 call = reinterpret_cast<CuteQDesignerMenuBarCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenuBar::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMenuBarCall1 call = reinterpret_cast<CuteQDesignerMenuBarCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenuBar::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMenuBarCall2 call = reinterpret_cast<CuteQDesignerMenuBarCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenuBar::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMenuBarCall3 call = reinterpret_cast<CuteQDesignerMenuBarCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenuBar::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMenuBarCall4 call = reinterpret_cast<CuteQDesignerMenuBarCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QDesignerMenuBar::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMenuBarCall5 call = reinterpret_cast<CuteQDesignerMenuBarCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::paintEvent(event);
  }

  //  void QDesignerMenuBar::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMenuBarCall6 call = reinterpret_cast<CuteQDesignerMenuBarCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::focusOutEvent(event);
  }

  //  void QDesignerMenuBar::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMenuBarCall7 call = reinterpret_cast<CuteQDesignerMenuBarCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::keyPressEvent(event);
  }

  //  void QDesignerMenuBar::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMenuBarCall8 call = reinterpret_cast<CuteQDesignerMenuBarCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenuBar::keyReleaseEvent(event);
  }

#if QT_CONFIG(menubar)
  //  QSize QMenuBar::sizeHint() const
  QSize sizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMenuBarCall9 call = reinterpret_cast<CuteQDesignerMenuBarCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMenuBar::sizeHint();
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  QSize QMenuBar::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMenuBarCall10 call = reinterpret_cast<CuteQDesignerMenuBarCall10>(taken[10]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMenuBar::minimumSizeHint();
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  int QMenuBar::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMenuBarCall11 call = reinterpret_cast<CuteQDesignerMenuBarCall11>(taken[11]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMenuBar::heightForWidth(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerMenuBarCall12 call = reinterpret_cast<CuteQDesignerMenuBarCall12>(taken[12]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QMenuBar::setVisible(visible);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerMenuBarCall13 call = reinterpret_cast<CuteQDesignerMenuBarCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::changeEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerMenuBarCall14 call = reinterpret_cast<CuteQDesignerMenuBarCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerMenuBarCall15 call = reinterpret_cast<CuteQDesignerMenuBarCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerMenuBarCall16 call = reinterpret_cast<CuteQDesignerMenuBarCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::leaveEvent(QEvent *a0)
  void leaveEvent(QEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerMenuBarCall17 call = reinterpret_cast<CuteQDesignerMenuBarCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::leaveEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerMenuBarCall18 call = reinterpret_cast<CuteQDesignerMenuBarCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::resizeEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if QT_CONFIG(menubar)
  //  void QMenuBar::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerMenuBarCall19 call = reinterpret_cast<CuteQDesignerMenuBarCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::focusInEvent(a0);
  }
#endif  // QT_CONFIG(menubar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
  //  void QMenuBar::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerMenuBarCall20 call = reinterpret_cast<CuteQDesignerMenuBarCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenuBar::timerEvent(a0);
  }
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
  //  bool QMenuBar::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerMenuBarCall21 call = reinterpret_cast<CuteQDesignerMenuBarCall21>(taken[21]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QMenuBar::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menubar)
  //  bool QMenuBar::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerMenuBarCall22 call = reinterpret_cast<CuteQDesignerMenuBarCall22>(taken[22]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMenuBar::event(a0);
  }
#endif  // QT_CONFIG(menubar)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(menubar)
  //  void QMenuBar::initStyleOption(QStyleOptionMenuItem *option, const
  //      QAction *action) const
  void initStyleOption(
      QStyleOptionMenuItem *option,
      const QAction *action) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerMenuBarCall23 call = reinterpret_cast<CuteQDesignerMenuBarCall23>(taken[23]);
      call(this, option, action, &handled);
      if (handled) return;
    }
    QMenuBar::initStyleOption(option, action);
  }
#endif  // QT_CONFIG(menubar)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerMenuBarCall24 call = reinterpret_cast<CuteQDesignerMenuBarCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerMenuBarCall25 call = reinterpret_cast<CuteQDesignerMenuBarCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerMenuBarCall26 call = reinterpret_cast<CuteQDesignerMenuBarCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerMenuBarCall27 call = reinterpret_cast<CuteQDesignerMenuBarCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDesignerMenuBarCall28 call = reinterpret_cast<CuteQDesignerMenuBarCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDesignerMenuBarCall29 call = reinterpret_cast<CuteQDesignerMenuBarCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDesignerMenuBarCall30 call = reinterpret_cast<CuteQDesignerMenuBarCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerMenuBarCall31 call = reinterpret_cast<CuteQDesignerMenuBarCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerMenuBarCall32 call = reinterpret_cast<CuteQDesignerMenuBarCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerMenuBarCall33 call = reinterpret_cast<CuteQDesignerMenuBarCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerMenuBarCall34 call = reinterpret_cast<CuteQDesignerMenuBarCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerMenuBarCall35 call = reinterpret_cast<CuteQDesignerMenuBarCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerMenuBarCall36 call = reinterpret_cast<CuteQDesignerMenuBarCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerMenuBarCall37 call = reinterpret_cast<CuteQDesignerMenuBarCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerMenuBarCall38 call = reinterpret_cast<CuteQDesignerMenuBarCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerMenuBarCall39 call = reinterpret_cast<CuteQDesignerMenuBarCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerMenuBarCall40 call = reinterpret_cast<CuteQDesignerMenuBarCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerMenuBarCall41 call = reinterpret_cast<CuteQDesignerMenuBarCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerMenuBarCall42 call = reinterpret_cast<CuteQDesignerMenuBarCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDesignerMenuBarCall43 call = reinterpret_cast<CuteQDesignerMenuBarCall43>(taken[43]);
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
      CuteQDesignerMenuBarCall44 call = reinterpret_cast<CuteQDesignerMenuBarCall44>(taken[44]);
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
      CuteQDesignerMenuBarCall45 call = reinterpret_cast<CuteQDesignerMenuBarCall45>(taken[45]);
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
      CuteQDesignerMenuBarCall46 call = reinterpret_cast<CuteQDesignerMenuBarCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QDesignerMenuBar10metaObjectEv(
    const QDesignerMenuBar *self) {
  return self->metaObject();
}

//  void *QDesignerMenuBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QDesignerMenuBar11qt_metacastEPKc(
    QDesignerMenuBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerMenuBar::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QDesignerMenuBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerMenuBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerMenuBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDesignerMenuBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerMenuBar::tr(s, c, n));
}

//  QDesignerMenuBar::QDesignerMenuBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerMenuBar *ritual_ZN16QDesignerMenuBarC1EP7QWidget(QWidget *parent) {
  return new CuteQDesignerMenuBar(parent);
}

//  QDesignerMenuBar::~QDesignerMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBarD1Ev(QDesignerMenuBar *self) {
  delete self;
}

//  bool QDesignerMenuBar::handleEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar11handleEventEP6QEvent(
    QDesignerMenuBar *self,
    QEvent *event) {
  return self->handleEvent(event);
}

//  QDesignerFormWindowInterface *QDesignerMenuBar::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK16QDesignerMenuBar10formWindowEv(
    const QDesignerMenuBar *self) {
  return self->formWindow();
}

//  QDesignerActionProviderExtension *QDesignerMenuBar::actionProvider()
extern "C" Q_DECL_EXPORT
QDesignerActionProviderExtension *ritual_ZN16QDesignerMenuBar14actionProviderEv(
    QDesignerMenuBar *self) {
  return self->actionProvider();
}

//  void QDesignerMenuBar::adjustSpecialActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar20adjustSpecialActionsEv(
    QDesignerMenuBar *self) {
  self->adjustSpecialActions();
}

//  bool QDesignerMenuBar::dragging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDesignerMenuBar8draggingEv(const QDesignerMenuBar *self) {
  return self->dragging();
}

//  void QDesignerMenuBar::moveLeft(bool ctrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar8moveLeftEb(
    QDesignerMenuBar *self,
    bool ctrl) {
  self->moveLeft(ctrl);
}

//  void QDesignerMenuBar::moveRight(bool ctrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar9moveRightEb(
    QDesignerMenuBar *self,
    bool ctrl) {
  self->moveRight(ctrl);
}

//  void QDesignerMenuBar::moveUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar6moveUpEv(QDesignerMenuBar *self) {
  self->moveUp();
}

//  void QDesignerMenuBar::moveDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar8moveDownEv(QDesignerMenuBar *self) {
  self->moveDown();
}

//  QList<QAction *> QDesignerMenuBar::contextMenuActions()
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZN16QDesignerMenuBar18contextMenuActionsEv(
    QDesignerMenuBar *self) {
  return new QList<QAction *>(self->contextMenuActions());
}

//  void QDesignerMenuBar::deleteMenuAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar16deleteMenuActionEP7QAction(
    QDesignerMenuBar *self,
    QAction *action) {
  self->deleteMenuAction(action);
}

//  void QDesignerMenuBar::deleteMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar10deleteMenuEv(QDesignerMenuBar *self) {
  self->deleteMenu();
}

//  void QDesignerMenuBar::slotRemoveMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar17slotRemoveMenuBarEv(
    QDesignerMenuBar *self) {
  self->slotRemoveMenuBar();
}

//  void QDesignerMenuBar::stopInlineEditing()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar17stopInlineEditingEv(
    QDesignerMenuBar *self) {
  self->stopInlineEditing();
}

//  void QDesignerMenuBar::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar11actionEventEP12QActionEvent(
    QDesignerMenuBar *self,
    QActionEvent *event) {
  self->actionEvent(event);
}

//  void QDesignerMenuBar::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar14dragEnterEventEP15QDragEnterEvent(
    QDesignerMenuBar *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}

//  void QDesignerMenuBar::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar13dragMoveEventEP14QDragMoveEvent(
    QDesignerMenuBar *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}

//  void QDesignerMenuBar::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar14dragLeaveEventEP15QDragLeaveEvent(
    QDesignerMenuBar *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QDesignerMenuBar::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar9dropEventEP10QDropEvent(
    QDesignerMenuBar *self,
    QDropEvent *event) {
  self->dropEvent(event);
}

//  void QDesignerMenuBar::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar10paintEventEP11QPaintEvent(
    QDesignerMenuBar *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QDesignerMenuBar::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar13focusOutEventEP11QFocusEvent(
    QDesignerMenuBar *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QDesignerMenuBar::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar13keyPressEventEP9QKeyEvent(
    QDesignerMenuBar *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QDesignerMenuBar::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar15keyReleaseEventEP9QKeyEvent(
    QDesignerMenuBar *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  bool QDesignerMenuBar::handleMouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar27handleMouseDoubleClickEventEP11QMouseEvent(
    QDesignerMenuBar *self,
    QMouseEvent *event) {
  return self->handleMouseDoubleClickEvent(event);
}

//  bool QDesignerMenuBar::handleMousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar21handleMousePressEventEP11QMouseEvent(
    QDesignerMenuBar *self,
    QMouseEvent *event) {
  return self->handleMousePressEvent(event);
}

//  bool QDesignerMenuBar::handleMouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar23handleMouseReleaseEventEP11QMouseEvent(
    QDesignerMenuBar *self,
    QMouseEvent *event) {
  return self->handleMouseReleaseEvent(event);
}

//  bool QDesignerMenuBar::handleMouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar20handleMouseMoveEventEP11QMouseEvent(
    QDesignerMenuBar *self,
    QMouseEvent *event) {
  return self->handleMouseMoveEvent(event);
}

//  bool QDesignerMenuBar::handleContextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar22handleContextMenuEventEP17QContextMenuEvent(
    QDesignerMenuBar *self,
    QContextMenuEvent *event) {
  return self->handleContextMenuEvent(event);
}

//  bool QDesignerMenuBar::handleKeyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar19handleKeyPressEventEP9QKeyEvent(
    QDesignerMenuBar *self,
    QKeyEvent *event) {
  return self->handleKeyPressEvent(event);
}

//  void QDesignerMenuBar::startDrag(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar9startDragERK6QPoint(
    QDesignerMenuBar *self,
    const QPoint *pos) {
  self->startDrag(*pos);
}

//  ActionDragCheck QDesignerMenuBar::checkAction(QAction *action) const
extern "C" Q_DECL_EXPORT
QDesignerMenuBar::ActionDragCheck ritual_ZNK16QDesignerMenuBar11checkActionEP7QAction(
    const QDesignerMenuBar *self,
    QAction *action) {
  return self->checkAction(action);
}

//  void QDesignerMenuBar::adjustIndicator(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar15adjustIndicatorERK6QPoint(
    QDesignerMenuBar *self,
    const QPoint *pos) {
  self->adjustIndicator(*pos);
}

//  int QDesignerMenuBar::findAction(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDesignerMenuBar10findActionERK6QPoint(
    const QDesignerMenuBar *self,
    const QPoint *pos) {
  return self->findAction(*pos);
}

//  QAction *QDesignerMenuBar::currentAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK16QDesignerMenuBar13currentActionEv(
    const QDesignerMenuBar *self) {
  return self->currentAction();
}

//  int QDesignerMenuBar::realActionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDesignerMenuBar15realActionCountEv(
    const QDesignerMenuBar *self) {
  return self->realActionCount();
}

//  void QDesignerMenuBar::enterEditMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar13enterEditModeEv(QDesignerMenuBar *self) {
  self->enterEditMode();
}

//  void QDesignerMenuBar::leaveEditMode(LeaveEditMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar13leaveEditModeENS_13LeaveEditModeE(
    QDesignerMenuBar *self,
    QDesignerMenuBar::LeaveEditMode mode) {
  self->leaveEditMode(mode);
}

//  void QDesignerMenuBar::showLineEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar12showLineEditEv(QDesignerMenuBar *self) {
  self->showLineEdit();
}

//  void QDesignerMenuBar::showMenu(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar8showMenuEi(
    QDesignerMenuBar *self,
    int index) {
  self->showMenu(index);
}

//  void QDesignerMenuBar::hideMenu(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar8hideMenuEi(
    QDesignerMenuBar *self,
    int index) {
  self->hideMenu(index);
}

//  QAction *QDesignerMenuBar::safeActionAt(int index) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK16QDesignerMenuBar12safeActionAtEi(
    const QDesignerMenuBar *self,
    int index) {
  return self->safeActionAt(index);
}

//  bool QDesignerMenuBar::swapActions(int a, int b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesignerMenuBar11swapActionsEii(
    QDesignerMenuBar *self,
    int a,
    int b) {
  return self->swapActions(a, b);
}

//  void QDesignerMenuBar::updateCurrentAction(bool selectAction)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar19updateCurrentActionEb(
    QDesignerMenuBar *self,
    bool selectAction) {
  self->updateCurrentAction(selectAction);
}

//  void QDesignerMenuBar::movePrevious(bool ctrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar12movePreviousEb(
    QDesignerMenuBar *self,
    bool ctrl) {
  self->movePrevious(ctrl);
}

//  void QDesignerMenuBar::moveNext(bool ctrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesignerMenuBar8moveNextEb(
    QDesignerMenuBar *self,
    bool ctrl) {
  self->moveNext(ctrl);
}

//  a Python function taken by a CuteQDesignerMenuBar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMenuBar(
    QDesignerMenuBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMenuBar *>(self)->take(key, call);
}

//  void QDesignerMenuBar::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar11actionEventEP12QActionEvent(
    QDesignerMenuBar *self,
    QActionEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::actionEvent(
      event);
}

//  void QDesignerMenuBar::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar14dragEnterEventEP15QDragEnterEvent(
    QDesignerMenuBar *self,
    QDragEnterEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::dragEnterEvent(
      event);
}

//  void QDesignerMenuBar::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar13dragMoveEventEP14QDragMoveEvent(
    QDesignerMenuBar *self,
    QDragMoveEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::dragMoveEvent(
      event);
}

//  void QDesignerMenuBar::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar14dragLeaveEventEP15QDragLeaveEvent(
    QDesignerMenuBar *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::dragLeaveEvent(
      event);
}

//  void QDesignerMenuBar::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar9dropEventEP10QDropEvent(
    QDesignerMenuBar *self,
    QDropEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::dropEvent(
      event);
}

//  void QDesignerMenuBar::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar10paintEventEP11QPaintEvent(
    QDesignerMenuBar *self,
    QPaintEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::paintEvent(
      event);
}

//  void QDesignerMenuBar::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar13focusOutEventEP11QFocusEvent(
    QDesignerMenuBar *self,
    QFocusEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::focusOutEvent(
      event);
}

//  void QDesignerMenuBar::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar13keyPressEventEP9QKeyEvent(
    QDesignerMenuBar *self,
    QKeyEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::keyPressEvent(
      event);
}

//  void QDesignerMenuBar::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDesignerMenuBar15keyReleaseEventEP9QKeyEvent(
    QDesignerMenuBar *self,
    QKeyEvent *event) {
  static_cast<OwnQDesignerMenuBar *>(self)->OwnQDesignerMenuBar::keyReleaseEvent(
      event);
}
