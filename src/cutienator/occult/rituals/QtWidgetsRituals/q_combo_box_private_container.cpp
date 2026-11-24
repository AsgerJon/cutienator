//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QComboBoxPrivateContainer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQComboBoxPrivateContainer : QComboBoxPrivateContainer {
  using QComboBoxPrivateContainer::changeEvent;
  using QComboBoxPrivateContainer::eventFilter;
  using QComboBoxPrivateContainer::mousePressEvent;
  using QComboBoxPrivateContainer::mouseReleaseEvent;
  using QComboBoxPrivateContainer::showEvent;
  using QComboBoxPrivateContainer::hideEvent;
  using QComboBoxPrivateContainer::timerEvent;
  using QComboBoxPrivateContainer::resizeEvent;
  using QComboBoxPrivateContainer::paintEvent;
};

//  A QComboBoxPrivateContainer that Python can take functions over in. Every QComboBoxPrivateContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef bool (*CuteQComboBoxPrivateContainerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall2)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall4)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall5)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall6)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall7)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateContainerCall8)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(combobox)
typedef const QSize * (*CuteQComboBoxPrivateContainerCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQComboBoxPrivateContainerCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateContainerCall11)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQComboBoxPrivateContainerCall12)(const void *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall13)(const void *, bool, int *);
typedef const QSize * (*CuteQComboBoxPrivateContainerCall14)(const void *, int *);
typedef int (*CuteQComboBoxPrivateContainerCall15)(const void *, int, int *);
typedef bool (*CuteQComboBoxPrivateContainerCall16)(const void *, int *);
typedef void * (*CuteQComboBoxPrivateContainerCall17)(const void *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall19)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQComboBoxPrivateContainerCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQComboBoxPrivateContainerCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall25)(const void *, QEnterEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall26)(const void *, QEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall27)(const void *, QMoveEvent *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall28)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQComboBoxPrivateContainerCall29)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQComboBoxPrivateContainerCall30)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQComboBoxPrivateContainerCall31)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateContainerCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateContainerCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateContainerCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateContainerCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQComboBoxPrivateContainerCall36)(const void *, int, int *);
typedef void (*CuteQComboBoxPrivateContainerCall37)(const void *, QPainter *, int *);
typedef void * (*CuteQComboBoxPrivateContainerCall38)(const void *, QPoint *, int *);
typedef void * (*CuteQComboBoxPrivateContainerCall39)(const void *, int *);
typedef void (*CuteQComboBoxPrivateContainerCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQComboBoxPrivateContainerCall41)(const void *, int, int *);
typedef bool (*CuteQComboBoxPrivateContainerCall42)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateContainerCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateContainerCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateContainerCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateContainerCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQComboBoxPrivateContainer : public QComboBoxPrivateContainer {
public:
  using QComboBoxPrivateContainer::QComboBoxPrivateContainer;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[28] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall0 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::changeEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
  //  bool QComboBoxPrivateContainer::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall1 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall1>(taken[1]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QComboBoxPrivateContainer::eventFilter(o, e);
  }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall2 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall2>(taken[2]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::mousePressEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall3 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::showEvent(QShowEvent *e)
  void showEvent(QShowEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall4 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::showEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::hideEvent(QHideEvent *e)
  void hideEvent(QHideEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall5 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::hideEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::timerEvent(QTimerEvent *timerEvent)
  void timerEvent(QTimerEvent *timerEvent) override {
    if (taken[6]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall6 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall6>(taken[6]);
      call(this, timerEvent, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::timerEvent(timerEvent);
  }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall7 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::resizeEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateContainer::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall8 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateContainer::paintEvent(e);
  }
#endif  // QT_CONFIG(combobox)

  //  QSize QFrame::sizeHint() const
  QSize sizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall9 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFrame::sizeHint();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QFrame::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall10 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall10>(taken[10]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QFrame::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall11 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall11>(taken[11]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall12 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[13]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall13 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall14 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall14>(taken[14]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall15 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall16 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall17 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall18 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall19 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall20 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall21 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall22 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall23 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall24 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall25 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall26 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall27 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall28 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall29 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall30 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall31 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall32 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall33 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall34 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall35 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall36 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall36>(taken[36]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall37 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall37>(taken[37]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall38 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall38>(taken[38]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall39 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall40 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall41 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQComboBoxPrivateContainerCall42 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall42>(taken[42]);
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
      CuteQComboBoxPrivateContainerCall43 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall43>(taken[43]);
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
      CuteQComboBoxPrivateContainerCall44 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall44>(taken[44]);
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
      CuteQComboBoxPrivateContainerCall45 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall45>(taken[45]);
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
      CuteQComboBoxPrivateContainerCall46 call = reinterpret_cast<CuteQComboBoxPrivateContainerCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QComboBoxPrivateContainer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QComboBoxPrivateContainer10metaObjectEv(
    const QComboBoxPrivateContainer *self) {
  return self->metaObject();
}

//  QString QComboBoxPrivateContainer::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QComboBoxPrivateContainer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QComboBoxPrivateContainer::tr(s, c, n));
}

//  QComboBoxPrivateContainer::QComboBoxPrivateContainer(QAbstractItemView
//      *itemView, QComboBox *parent)
extern "C" Q_DECL_EXPORT
QComboBoxPrivateContainer *ritual_ZN25QComboBoxPrivateContainerC1EP17QAbstractItemViewP9QComboBox(
    QAbstractItemView *itemView,
    QComboBox *parent) {
  return new CuteQComboBoxPrivateContainer(itemView, parent);
}

//  QComboBoxPrivateContainer::~QComboBoxPrivateContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainerD1Ev(
    QComboBoxPrivateContainer *self) {
  delete self;
}

//  QAbstractItemView *QComboBoxPrivateContainer::itemView() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK25QComboBoxPrivateContainer8itemViewEv(
    const QComboBoxPrivateContainer *self) {
  return self->itemView();
}

//  void QComboBoxPrivateContainer::setItemView(QAbstractItemView *itemView)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer11setItemViewEP17QAbstractItemView(
    QComboBoxPrivateContainer *self,
    QAbstractItemView *itemView) {
  self->setItemView(itemView);
}

//  int QComboBoxPrivateContainer::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QComboBoxPrivateContainer7spacingEv(
    const QComboBoxPrivateContainer *self) {
  return self->spacing();
}

//  int QComboBoxPrivateContainer::topMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QComboBoxPrivateContainer9topMarginEv(
    const QComboBoxPrivateContainer *self) {
  return self->topMargin();
}

//  int QComboBoxPrivateContainer::bottomMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QComboBoxPrivateContainer12bottomMarginEv(
    const QComboBoxPrivateContainer *self) {
  return self->bottomMargin();
}

//  void QComboBoxPrivateContainer::updateTopBottomMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer21updateTopBottomMarginEv(
    QComboBoxPrivateContainer *self) {
  self->updateTopBottomMargin();
}

//  void QComboBoxPrivateContainer::updateStyleSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer19updateStyleSettingsEv(
    QComboBoxPrivateContainer *self) {
  self->updateStyleSettings();
}

//  void QComboBoxPrivateContainer::scrollItemView(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer14scrollItemViewEi(
    QComboBoxPrivateContainer *self,
    int action) {
  self->scrollItemView(action);
}

//  void QComboBoxPrivateContainer::hideScrollers()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer13hideScrollersEv(
    QComboBoxPrivateContainer *self) {
  self->hideScrollers();
}

//  void QComboBoxPrivateContainer::updateScrollers()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer15updateScrollersEv(
    QComboBoxPrivateContainer *self) {
  self->updateScrollers();
}

//  void QComboBoxPrivateContainer::viewDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer13viewDestroyedEv(
    QComboBoxPrivateContainer *self) {
  self->viewDestroyed();
}

//  void QComboBoxPrivateContainer::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer11changeEventEP6QEvent(
    QComboBoxPrivateContainer *self,
    QEvent *e) {
  self->changeEvent(e);
}

//  bool QComboBoxPrivateContainer::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QComboBoxPrivateContainer11eventFilterEP7QObjectP6QEvent(
    QComboBoxPrivateContainer *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  void QComboBoxPrivateContainer::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer15mousePressEventEP11QMouseEvent(
    QComboBoxPrivateContainer *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QComboBoxPrivateContainer::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer17mouseReleaseEventEP11QMouseEvent(
    QComboBoxPrivateContainer *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

//  void QComboBoxPrivateContainer::showEvent(QShowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer9showEventEP10QShowEvent(
    QComboBoxPrivateContainer *self,
    QShowEvent *e) {
  self->showEvent(e);
}

//  void QComboBoxPrivateContainer::hideEvent(QHideEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer9hideEventEP10QHideEvent(
    QComboBoxPrivateContainer *self,
    QHideEvent *e) {
  self->hideEvent(e);
}

//  void QComboBoxPrivateContainer::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer10timerEventEP11QTimerEvent(
    QComboBoxPrivateContainer *self,
    QTimerEvent *timerEvent) {
  self->timerEvent(timerEvent);
}

//  void QComboBoxPrivateContainer::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer11resizeEventEP12QResizeEvent(
    QComboBoxPrivateContainer *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  void QComboBoxPrivateContainer::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QComboBoxPrivateContainer10paintEventEP11QPaintEvent(
    QComboBoxPrivateContainer *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  QStyleOptionComboBox QComboBoxPrivateContainer::comboStyleOption() const
extern "C" Q_DECL_EXPORT
QStyleOptionComboBox *ritual_ZNK25QComboBoxPrivateContainer16comboStyleOptionEv(
    const QComboBoxPrivateContainer *self) {
  return new QStyleOptionComboBox(self->comboStyleOption());
}

//  a Python function taken by a CuteQComboBoxPrivateContainer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboBoxPrivateContainer(
    QComboBoxPrivateContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQComboBoxPrivateContainer *>(self)->take(key, call);
}

//  void QComboBoxPrivateContainer::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer11changeEventEP6QEvent(
    QComboBoxPrivateContainer *self,
    QEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::changeEvent(
      e);
}

//  bool QComboBoxPrivateContainer::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QComboBoxPrivateContainer11eventFilterEP7QObjectP6QEvent(
    QComboBoxPrivateContainer *self,
    QObject *o,
    QEvent *e) {
  return static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::eventFilter(
      o,
      e);
}

//  void QComboBoxPrivateContainer::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer15mousePressEventEP11QMouseEvent(
    QComboBoxPrivateContainer *self,
    QMouseEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::mousePressEvent(
      e);
}

//  void QComboBoxPrivateContainer::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer17mouseReleaseEventEP11QMouseEvent(
    QComboBoxPrivateContainer *self,
    QMouseEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::mouseReleaseEvent(
      e);
}

//  void QComboBoxPrivateContainer::showEvent(QShowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer9showEventEP10QShowEvent(
    QComboBoxPrivateContainer *self,
    QShowEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::showEvent(
      e);
}

//  void QComboBoxPrivateContainer::hideEvent(QHideEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer9hideEventEP10QHideEvent(
    QComboBoxPrivateContainer *self,
    QHideEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::hideEvent(
      e);
}

//  void QComboBoxPrivateContainer::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer10timerEventEP11QTimerEvent(
    QComboBoxPrivateContainer *self,
    QTimerEvent *timerEvent) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::timerEvent(
      timerEvent);
}

//  void QComboBoxPrivateContainer::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer11resizeEventEP12QResizeEvent(
    QComboBoxPrivateContainer *self,
    QResizeEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::resizeEvent(
      e);
}

//  void QComboBoxPrivateContainer::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QComboBoxPrivateContainer10paintEventEP11QPaintEvent(
    QComboBoxPrivateContainer *self,
    QPaintEvent *e) {
  static_cast<OwnQComboBoxPrivateContainer *>(self)->OwnQComboBoxPrivateContainer::paintEvent(
      e);
}

#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(combobox)
