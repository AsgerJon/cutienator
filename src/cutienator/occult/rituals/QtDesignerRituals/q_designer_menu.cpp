//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_menu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_menu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDesignerMenu may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDesignerMenu : QDesignerMenu {
  using QDesignerMenu::actionEvent;
  using QDesignerMenu::dragEnterEvent;
  using QDesignerMenu::dragMoveEvent;
  using QDesignerMenu::dragLeaveEvent;
  using QDesignerMenu::dropEvent;
  using QDesignerMenu::paintEvent;
  using QDesignerMenu::keyPressEvent;
  using QDesignerMenu::keyReleaseEvent;
  using QDesignerMenu::showEvent;
};

//  A QDesignerMenu that Python can take functions over in. Every QDesignerMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDesignerMenuCall0)(const void *, bool, int *);
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerMenuCall1)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuCall2)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuCall3)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuCall4)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuCall5)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerMenuCall6)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerMenuCall7)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerMenuCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerMenuCall9)(const void *, QShowEvent *, int *);
#if QT_CONFIG(menu)
typedef const QSize * (*CuteQDesignerMenuCall10)(const void *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall12)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall13)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall16)(const void *, QEnterEvent *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall18)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(menu)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall19)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
typedef bool (*CuteQDesignerMenuCall20)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
typedef bool (*CuteQDesignerMenuCall21)(const void *, bool, int *);
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
typedef void (*CuteQDesignerMenuCall22)(const void *, QStyleOptionMenuItem *, const QAction *, int *);
#endif  // QT_CONFIG(menu)
typedef int (*CuteQDesignerMenuCall23)(const void *, int *);
typedef const QSize * (*CuteQDesignerMenuCall24)(const void *, int *);
typedef int (*CuteQDesignerMenuCall25)(const void *, int, int *);
typedef bool (*CuteQDesignerMenuCall26)(const void *, int *);
typedef void * (*CuteQDesignerMenuCall27)(const void *, int *);
typedef void (*CuteQDesignerMenuCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerMenuCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerMenuCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerMenuCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerMenuCall32)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerMenuCall33)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerMenuCall34)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerMenuCall35)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef int (*CuteQDesignerMenuCall36)(const void *, int, int *);
typedef void (*CuteQDesignerMenuCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerMenuCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerMenuCall39)(const void *, int *);
typedef void (*CuteQDesignerMenuCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerMenuCall41)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMenuCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMenuCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerMenu : public QDesignerMenu {
public:
  using QDesignerMenu::QDesignerMenu;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK5QMenu15initStyleOptionEP20QStyleOptionMenuItemPK7QAction")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[33] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
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

  //  void QDesignerMenu::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMenuCall0 call = reinterpret_cast<CuteQDesignerMenuCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDesignerMenu::setVisible(visible);
  }

#if !defined(QT_NO_ACTION)
  //  void QDesignerMenu::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMenuCall1 call = reinterpret_cast<CuteQDesignerMenuCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenu::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMenuCall2 call = reinterpret_cast<CuteQDesignerMenuCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenu::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMenuCall3 call = reinterpret_cast<CuteQDesignerMenuCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenu::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMenuCall4 call = reinterpret_cast<CuteQDesignerMenuCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QDesignerMenu::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMenuCall5 call = reinterpret_cast<CuteQDesignerMenuCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QDesignerMenu::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMenuCall6 call = reinterpret_cast<CuteQDesignerMenuCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::paintEvent(event);
  }

  //  void QDesignerMenu::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMenuCall7 call = reinterpret_cast<CuteQDesignerMenuCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::keyPressEvent(event);
  }

  //  void QDesignerMenu::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMenuCall8 call = reinterpret_cast<CuteQDesignerMenuCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::keyReleaseEvent(event);
  }

  //  void QDesignerMenu::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMenuCall9 call = reinterpret_cast<CuteQDesignerMenuCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDesignerMenu::showEvent(event);
  }

#if QT_CONFIG(menu)
  //  QSize QMenu::sizeHint() const
  QSize sizeHint() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMenuCall10 call = reinterpret_cast<CuteQDesignerMenuCall10>(taken[10]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMenu::sizeHint();
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMenuCall11 call = reinterpret_cast<CuteQDesignerMenuCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::changeEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerMenuCall12 call = reinterpret_cast<CuteQDesignerMenuCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerMenuCall13 call = reinterpret_cast<CuteQDesignerMenuCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerMenuCall14 call = reinterpret_cast<CuteQDesignerMenuCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(menu)
  //  void QMenu::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerMenuCall15 call = reinterpret_cast<CuteQDesignerMenuCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::wheelEvent(a0);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(menu)
  //  void QMenu::enterEvent(QEnterEvent *a0)
  void enterEvent(QEnterEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerMenuCall16 call = reinterpret_cast<CuteQDesignerMenuCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::enterEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::leaveEvent(QEvent *a0)
  void leaveEvent(QEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerMenuCall17 call = reinterpret_cast<CuteQDesignerMenuCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::leaveEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerMenuCall18 call = reinterpret_cast<CuteQDesignerMenuCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::hideEvent(a0);
  }
#endif  // QT_CONFIG(menu)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
  //  void QMenu::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerMenuCall19 call = reinterpret_cast<CuteQDesignerMenuCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMenu::timerEvent(a0);
  }
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(menu)
  //  bool QMenu::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerMenuCall20 call = reinterpret_cast<CuteQDesignerMenuCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMenu::event(a0);
  }
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(menu)
  //  bool QMenu::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerMenuCall21 call = reinterpret_cast<CuteQDesignerMenuCall21>(taken[21]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QMenu::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
  //  void QMenu::initStyleOption(QStyleOptionMenuItem *option, const
  //      QAction *action) const
  void initStyleOption(
      QStyleOptionMenuItem *option,
      const QAction *action) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerMenuCall22 call = reinterpret_cast<CuteQDesignerMenuCall22>(taken[22]);
      call(this, option, action, &handled);
      if (handled) return;
    }
    QMenu::initStyleOption(option, action);
  }
#endif  // QT_CONFIG(menu)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerMenuCall23 call = reinterpret_cast<CuteQDesignerMenuCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerMenuCall24 call = reinterpret_cast<CuteQDesignerMenuCall24>(taken[24]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerMenuCall25 call = reinterpret_cast<CuteQDesignerMenuCall25>(taken[25]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerMenuCall26 call = reinterpret_cast<CuteQDesignerMenuCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerMenuCall27 call = reinterpret_cast<CuteQDesignerMenuCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDesignerMenuCall28 call = reinterpret_cast<CuteQDesignerMenuCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDesignerMenuCall29 call = reinterpret_cast<CuteQDesignerMenuCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDesignerMenuCall30 call = reinterpret_cast<CuteQDesignerMenuCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerMenuCall31 call = reinterpret_cast<CuteQDesignerMenuCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerMenuCall32 call = reinterpret_cast<CuteQDesignerMenuCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerMenuCall33 call = reinterpret_cast<CuteQDesignerMenuCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerMenuCall34 call = reinterpret_cast<CuteQDesignerMenuCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerMenuCall35 call = reinterpret_cast<CuteQDesignerMenuCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerMenuCall36 call = reinterpret_cast<CuteQDesignerMenuCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerMenuCall37 call = reinterpret_cast<CuteQDesignerMenuCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerMenuCall38 call = reinterpret_cast<CuteQDesignerMenuCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerMenuCall39 call = reinterpret_cast<CuteQDesignerMenuCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerMenuCall40 call = reinterpret_cast<CuteQDesignerMenuCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerMenuCall41 call = reinterpret_cast<CuteQDesignerMenuCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerMenuCall42 call = reinterpret_cast<CuteQDesignerMenuCall42>(taken[42]);
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
      CuteQDesignerMenuCall43 call = reinterpret_cast<CuteQDesignerMenuCall43>(taken[43]);
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
      CuteQDesignerMenuCall44 call = reinterpret_cast<CuteQDesignerMenuCall44>(taken[44]);
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
      CuteQDesignerMenuCall45 call = reinterpret_cast<CuteQDesignerMenuCall45>(taken[45]);
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
      CuteQDesignerMenuCall46 call = reinterpret_cast<CuteQDesignerMenuCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QDesignerMenu10metaObjectEv(
    const QDesignerMenu *self) {
  return self->metaObject();
}

//  void *QDesignerMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QDesignerMenu11qt_metacastEPKc(
    QDesignerMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerMenu::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QDesignerMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerMenu::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QDesignerMenu2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerMenu::tr(s, c, n));
}

//  QDesignerMenu::QDesignerMenu(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerMenu *ritual_ZN13QDesignerMenuC1EP7QWidget(QWidget *parent) {
  return new CuteQDesignerMenu(parent);
}

//  QDesignerMenu::~QDesignerMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenuD1Ev(QDesignerMenu *self) {
  delete self;
}

//  bool QDesignerMenu::handleEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu11handleEventEP6QEvent(
    QDesignerMenu *self,
    QEvent *event) {
  return self->handleEvent(event);
}

//  void QDesignerMenu::deactivateMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu14deactivateMenuEv(QDesignerMenu *self) {
  self->deactivateMenu();
}

//  QDesignerFormWindowInterface *QDesignerMenu::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK13QDesignerMenu10formWindowEv(
    const QDesignerMenu *self) {
  return self->formWindow();
}

//  QDesignerActionProviderExtension *QDesignerMenu::actionProvider()
extern "C" Q_DECL_EXPORT
QDesignerActionProviderExtension *ritual_ZN13QDesignerMenu14actionProviderEv(
    QDesignerMenu *self) {
  return self->actionProvider();
}

//  QDesignerMenu *QDesignerMenu::parentMenu() const
extern "C" Q_DECL_EXPORT
QDesignerMenu *ritual_ZNK13QDesignerMenu10parentMenuEv(
    const QDesignerMenu *self) {
  return self->parentMenu();
}

//  QDesignerMenuBar *QDesignerMenu::parentMenuBar() const
extern "C" Q_DECL_EXPORT
QDesignerMenuBar *ritual_ZNK13QDesignerMenu13parentMenuBarEv(
    const QDesignerMenu *self) {
  return self->parentMenuBar();
}

//  void QDesignerMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu10setVisibleEb(
    QDesignerMenu *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QDesignerMenu::adjustSpecialActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu20adjustSpecialActionsEv(QDesignerMenu *self) {
  self->adjustSpecialActions();
}

//  void QDesignerMenu::createRealMenuAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu20createRealMenuActionEP7QAction(
    QDesignerMenu *self,
    QAction *action) {
  self->createRealMenuAction(action);
}

//  void QDesignerMenu::removeRealMenu(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu14removeRealMenuEP7QAction(
    QDesignerMenu *self,
    QAction *action) {
  self->removeRealMenu(action);
}

//  void QDesignerMenu::drawSelection(QPainter *p, const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu13drawSelectionEP8QPainterRK5QRect(
    QPainter *p,
    const QRect *r) {
  QDesignerMenu::drawSelection(p, *r);
}

//  bool QDesignerMenu::dragging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDesignerMenu8draggingEv(const QDesignerMenu *self) {
  return self->dragging();
}

//  void QDesignerMenu::closeMenuChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu14closeMenuChainEv(QDesignerMenu *self) {
  self->closeMenuChain();
}

//  void QDesignerMenu::moveLeft()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu8moveLeftEv(QDesignerMenu *self) {
  self->moveLeft();
}

//  void QDesignerMenu::moveRight()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu9moveRightEv(QDesignerMenu *self) {
  self->moveRight();
}

//  void QDesignerMenu::moveUp(bool ctrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu6moveUpEb(QDesignerMenu *self, bool ctrl) {
  self->moveUp(ctrl);
}

//  void QDesignerMenu::moveDown(bool ctrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu8moveDownEb(QDesignerMenu *self, bool ctrl) {
  self->moveDown(ctrl);
}

//  void QDesignerMenu::deleteAction(QAction *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu12deleteActionEP7QAction(
    QDesignerMenu *self,
    QAction *a) {
  self->deleteAction(a);
}

//  void QDesignerMenu::slotAddSeparator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu16slotAddSeparatorEv(QDesignerMenu *self) {
  self->slotAddSeparator();
}

//  void QDesignerMenu::slotRemoveSelectedAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu24slotRemoveSelectedActionEv(
    QDesignerMenu *self) {
  self->slotRemoveSelectedAction();
}

//  void QDesignerMenu::slotShowSubMenuNow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu18slotShowSubMenuNowEv(QDesignerMenu *self) {
  self->slotShowSubMenuNow();
}

//  void QDesignerMenu::slotDeactivateNow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu17slotDeactivateNowEv(QDesignerMenu *self) {
  self->slotDeactivateNow();
}

//  void QDesignerMenu::slotAdjustSizeNow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu17slotAdjustSizeNowEv(QDesignerMenu *self) {
  self->slotAdjustSizeNow();
}

//  void QDesignerMenu::stopInlineEditing()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu17stopInlineEditingEv(QDesignerMenu *self) {
  self->stopInlineEditing();
}

//  void QDesignerMenu::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu11actionEventEP12QActionEvent(
    QDesignerMenu *self,
    QActionEvent *event) {
  self->actionEvent(event);
}

//  void QDesignerMenu::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu14dragEnterEventEP15QDragEnterEvent(
    QDesignerMenu *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}

//  void QDesignerMenu::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu13dragMoveEventEP14QDragMoveEvent(
    QDesignerMenu *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}

//  void QDesignerMenu::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu14dragLeaveEventEP15QDragLeaveEvent(
    QDesignerMenu *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QDesignerMenu::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu9dropEventEP10QDropEvent(
    QDesignerMenu *self,
    QDropEvent *event) {
  self->dropEvent(event);
}

//  void QDesignerMenu::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu10paintEventEP11QPaintEvent(
    QDesignerMenu *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QDesignerMenu::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu13keyPressEventEP9QKeyEvent(
    QDesignerMenu *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QDesignerMenu::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu15keyReleaseEventEP9QKeyEvent(
    QDesignerMenu *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QDesignerMenu::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu9showEventEP10QShowEvent(
    QDesignerMenu *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  bool QDesignerMenu::handleMouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu27handleMouseDoubleClickEventEP11QMouseEvent(
    QDesignerMenu *self,
    QMouseEvent *event) {
  return self->handleMouseDoubleClickEvent(event);
}

//  bool QDesignerMenu::handleMousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu21handleMousePressEventEP11QMouseEvent(
    QDesignerMenu *self,
    QMouseEvent *event) {
  return self->handleMousePressEvent(event);
}

//  bool QDesignerMenu::handleMouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu23handleMouseReleaseEventEP11QMouseEvent(
    QDesignerMenu *self,
    QMouseEvent *event) {
  return self->handleMouseReleaseEvent(event);
}

//  bool QDesignerMenu::handleMouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu20handleMouseMoveEventEP11QMouseEvent(
    QDesignerMenu *self,
    QMouseEvent *event) {
  return self->handleMouseMoveEvent(event);
}

//  bool QDesignerMenu::handleContextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu22handleContextMenuEventEP17QContextMenuEvent(
    QDesignerMenu *self,
    QContextMenuEvent *event) {
  return self->handleContextMenuEvent(event);
}

//  bool QDesignerMenu::handleKeyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu19handleKeyPressEventEP9QKeyEvent(
    QDesignerMenu *self,
    QKeyEvent *event) {
  return self->handleKeyPressEvent(event);
}

//  void QDesignerMenu::startDrag(const QPoint &pos, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu9startDragERK6QPoint6QFlagsIN2Qt16KeyboardModifierEE(
    QDesignerMenu *self,
    const QPoint *pos,
    int modifiers) {
  self->startDrag(*pos, QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  void QDesignerMenu::adjustIndicator(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu15adjustIndicatorERK6QPoint(
    QDesignerMenu *self,
    const QPoint *pos) {
  self->adjustIndicator(*pos);
}

//  int QDesignerMenu::findAction(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDesignerMenu10findActionERK6QPoint(
    const QDesignerMenu *self,
    const QPoint *pos) {
  return self->findAction(*pos);
}

//  QAction *QDesignerMenu::currentAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK13QDesignerMenu13currentActionEv(
    const QDesignerMenu *self) {
  return self->currentAction();
}

//  int QDesignerMenu::realActionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDesignerMenu15realActionCountEv(const QDesignerMenu *self) {
  return self->realActionCount();
}

//  ActionDragCheck QDesignerMenu::checkAction(QAction *action) const
extern "C" Q_DECL_EXPORT
QDesignerMenu::ActionDragCheck ritual_ZNK13QDesignerMenu11checkActionEP7QAction(
    const QDesignerMenu *self,
    QAction *action) {
  return self->checkAction(action);
}

//  void QDesignerMenu::showSubMenu(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu11showSubMenuEP7QAction(
    QDesignerMenu *self,
    QAction *action) {
  self->showSubMenu(action);
}

//  void QDesignerMenu::enterEditMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu13enterEditModeEv(QDesignerMenu *self) {
  self->enterEditMode();
}

//  void QDesignerMenu::leaveEditMode(LeaveEditMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu13leaveEditModeENS_13LeaveEditModeE(
    QDesignerMenu *self,
    QDesignerMenu::LeaveEditMode mode) {
  self->leaveEditMode(mode);
}

//  void QDesignerMenu::showLineEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu12showLineEditEv(QDesignerMenu *self) {
  self->showLineEdit();
}

//  QAction *QDesignerMenu::createAction(const QString &text, bool separator)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN13QDesignerMenu12createActionERK7QStringb(
    QDesignerMenu *self,
    const QString *text,
    bool separator) {
  return self->createAction(*text, separator);
}

//  QDesignerMenu *QDesignerMenu::findOrCreateSubMenu(QAction *action)
extern "C" Q_DECL_EXPORT
QDesignerMenu *ritual_ZN13QDesignerMenu19findOrCreateSubMenuEP7QAction(
    QDesignerMenu *self,
    QAction *action) {
  return self->findOrCreateSubMenu(action);
}

//  QAction *QDesignerMenu::safeActionAt(int index) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK13QDesignerMenu12safeActionAtEi(
    const QDesignerMenu *self,
    int index) {
  return self->safeActionAt(index);
}

//  QAction *QDesignerMenu::safeMenuAction(QDesignerMenu *menu) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK13QDesignerMenu14safeMenuActionEPS_(
    const QDesignerMenu *self,
    QDesignerMenu *menu) {
  return self->safeMenuAction(menu);
}

//  bool QDesignerMenu::swap(int a, int b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu4swapEii(QDesignerMenu *self, int a, int b) {
  return self->swap(a, b);
}

//  void QDesignerMenu::hideSubMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu11hideSubMenuEv(QDesignerMenu *self) {
  self->hideSubMenu();
}

//  void QDesignerMenu::deleteAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu12deleteActionEv(QDesignerMenu *self) {
  self->deleteAction();
}

//  bool QDesignerMenu::canCreateSubMenu(QAction *action) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDesignerMenu16canCreateSubMenuEP7QAction(
    const QDesignerMenu *self,
    QAction *action) {
  return self->canCreateSubMenu(action);
}

//  QDesignerMenu *QDesignerMenu::findRootMenu() const
extern "C" Q_DECL_EXPORT
QDesignerMenu *ritual_ZNK13QDesignerMenu12findRootMenuEv(
    const QDesignerMenu *self) {
  return self->findRootMenu();
}

//  QDesignerMenu *QDesignerMenu::findActivatedMenu() const
extern "C" Q_DECL_EXPORT
QDesignerMenu *ritual_ZNK13QDesignerMenu17findActivatedMenuEv(
    const QDesignerMenu *self) {
  return self->findActivatedMenu();
}

//  QRect QDesignerMenu::subMenuPixmapRect(QAction *action) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QDesignerMenu17subMenuPixmapRectEP7QAction(
    const QDesignerMenu *self,
    QAction *action) {
  return new QRect(self->subMenuPixmapRect(action));
}

//  bool QDesignerMenu::hasSubMenuPixmap(QAction *action) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDesignerMenu16hasSubMenuPixmapEP7QAction(
    const QDesignerMenu *self,
    QAction *action) {
  return self->hasSubMenuPixmap(action);
}

//  void QDesignerMenu::selectCurrentAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDesignerMenu19selectCurrentActionEv(QDesignerMenu *self) {
  self->selectCurrentAction();
}

//  bool QDesignerMenu::hideSubMenuOnCursorKey()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu22hideSubMenuOnCursorKeyEv(
    QDesignerMenu *self) {
  return self->hideSubMenuOnCursorKey();
}

//  bool QDesignerMenu::showSubMenuOnCursorKey()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDesignerMenu22showSubMenuOnCursorKeyEv(
    QDesignerMenu *self) {
  return self->showSubMenuOnCursorKey();
}

//  a Python function taken by a CuteQDesignerMenu, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMenu(
    QDesignerMenu *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMenu *>(self)->take(key, call);
}

//  void QDesignerMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu10setVisibleEb(
    QDesignerMenu *self,
    bool visible) {
  self->QDesignerMenu::setVisible(visible);
}

//  void QDesignerMenu::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu11actionEventEP12QActionEvent(
    QDesignerMenu *self,
    QActionEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::actionEvent(
      event);
}

//  void QDesignerMenu::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu14dragEnterEventEP15QDragEnterEvent(
    QDesignerMenu *self,
    QDragEnterEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::dragEnterEvent(
      event);
}

//  void QDesignerMenu::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu13dragMoveEventEP14QDragMoveEvent(
    QDesignerMenu *self,
    QDragMoveEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::dragMoveEvent(
      event);
}

//  void QDesignerMenu::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu14dragLeaveEventEP15QDragLeaveEvent(
    QDesignerMenu *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::dragLeaveEvent(
      event);
}

//  void QDesignerMenu::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu9dropEventEP10QDropEvent(
    QDesignerMenu *self,
    QDropEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::dropEvent(event);
}

//  void QDesignerMenu::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu10paintEventEP11QPaintEvent(
    QDesignerMenu *self,
    QPaintEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::paintEvent(event);
}

//  void QDesignerMenu::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu13keyPressEventEP9QKeyEvent(
    QDesignerMenu *self,
    QKeyEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::keyPressEvent(
      event);
}

//  void QDesignerMenu::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu15keyReleaseEventEP9QKeyEvent(
    QDesignerMenu *self,
    QKeyEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::keyReleaseEvent(
      event);
}

//  void QDesignerMenu::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QDesignerMenu9showEventEP10QShowEvent(
    QDesignerMenu *self,
    QShowEvent *event) {
  static_cast<OwnQDesignerMenu *>(self)->OwnQDesignerMenu::showEvent(event);
}
