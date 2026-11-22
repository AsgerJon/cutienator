//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdial.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdial.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDial : QDial {
  using QDial::event;
  using QDial::resizeEvent;
  using QDial::paintEvent;
  using QDial::mousePressEvent;
  using QDial::mouseReleaseEvent;
  using QDial::mouseMoveEvent;
  using QDial::initStyleOption;
};

//  A QDial that Python can take functions over in. Every QDial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQDialCall0)(const void *, int *);
typedef const QSize * (*CuteQDialCall1)(const void *, int *);
typedef bool (*CuteQDialCall2)(const void *, QEvent *, int *);
typedef void (*CuteQDialCall3)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDialCall4)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDialCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialCall6)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialCall8)(const void *, QStyleOptionSlider *, int *);
typedef void (*CuteQDialCall9)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDialCall10)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDialCall11)(const void *, QWheelEvent *, int *);
typedef void (*CuteQDialCall12)(const void *, QEvent *, int *);
typedef int (*CuteQDialCall13)(const void *, int *);
typedef void (*CuteQDialCall14)(const void *, bool, int *);
typedef int (*CuteQDialCall15)(const void *, int, int *);
typedef bool (*CuteQDialCall16)(const void *, int *);
typedef void * (*CuteQDialCall17)(const void *, int *);
typedef void (*CuteQDialCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDialCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDialCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDialCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDialCall23)(const void *, QEvent *, int *);
typedef void (*CuteQDialCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDialCall25)(const void *, QCloseEvent *, int *);
typedef void (*CuteQDialCall26)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQDialCall27)(const void *, QTabletEvent *, int *);
typedef void (*CuteQDialCall28)(const void *, QActionEvent *, int *);
typedef void (*CuteQDialCall29)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQDialCall30)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQDialCall31)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQDialCall32)(const void *, QDropEvent *, int *);
typedef void (*CuteQDialCall33)(const void *, QShowEvent *, int *);
typedef void (*CuteQDialCall34)(const void *, QHideEvent *, int *);
typedef int (*CuteQDialCall35)(const void *, int, int *);
typedef void (*CuteQDialCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQDialCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQDialCall38)(const void *, int *);
typedef void (*CuteQDialCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDialCall40)(const void *, int, int *);
typedef bool (*CuteQDialCall41)(const void *, bool, int *);
typedef bool (*CuteQDialCall42)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDialCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQDialCall44)(const void *, QEvent *, int *);
typedef void (*CuteQDialCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDialCall46)(const void *, const QMetaMethod *, int *);
class CuteQDial : public QDial {
public:
  using QDial::QDial;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK5QDial15initStyleOptionEP18QStyleOptionSlider")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  QSize QDial::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDialCall0 call = reinterpret_cast<CuteQDialCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDial::sizeHint();
  }

  //  QSize QDial::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDialCall1 call = reinterpret_cast<CuteQDialCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDial::minimumSizeHint();
  }

  //  bool QDial::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDialCall2 call = reinterpret_cast<CuteQDialCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QDial::event(e);
  }

  //  void QDial::resizeEvent(QResizeEvent *re)
  void resizeEvent(QResizeEvent *re) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDialCall3 call = reinterpret_cast<CuteQDialCall3>(taken[3]);
      call(this, re, &handled);
      if (handled) return;
    }
    QDial::resizeEvent(re);
  }

  //  void QDial::paintEvent(QPaintEvent *pe)
  void paintEvent(QPaintEvent *pe) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDialCall4 call = reinterpret_cast<CuteQDialCall4>(taken[4]);
      call(this, pe, &handled);
      if (handled) return;
    }
    QDial::paintEvent(pe);
  }

  //  void QDial::mousePressEvent(QMouseEvent *me)
  void mousePressEvent(QMouseEvent *me) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDialCall5 call = reinterpret_cast<CuteQDialCall5>(taken[5]);
      call(this, me, &handled);
      if (handled) return;
    }
    QDial::mousePressEvent(me);
  }

  //  void QDial::mouseReleaseEvent(QMouseEvent *me)
  void mouseReleaseEvent(QMouseEvent *me) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDialCall6 call = reinterpret_cast<CuteQDialCall6>(taken[6]);
      call(this, me, &handled);
      if (handled) return;
    }
    QDial::mouseReleaseEvent(me);
  }

  //  void QDial::mouseMoveEvent(QMouseEvent *me)
  void mouseMoveEvent(QMouseEvent *me) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDialCall7 call = reinterpret_cast<CuteQDialCall7>(taken[7]);
      call(this, me, &handled);
      if (handled) return;
    }
    QDial::mouseMoveEvent(me);
  }

  //  void QDial::initStyleOption(QStyleOptionSlider *option) const
  void initStyleOption(QStyleOptionSlider *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDialCall8 call = reinterpret_cast<CuteQDialCall8>(taken[8]);
      call(this, option, &handled);
      if (handled) return;
    }
    QDial::initStyleOption(option);
  }

  //  void QAbstractSlider::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDialCall9 call = reinterpret_cast<CuteQDialCall9>(taken[9]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QAbstractSlider::keyPressEvent(ev);
  }

  //  void QAbstractSlider::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDialCall10 call = reinterpret_cast<CuteQDialCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractSlider::timerEvent(a0);
  }

  //  void QAbstractSlider::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDialCall11 call = reinterpret_cast<CuteQDialCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::wheelEvent(e);
  }

  //  void QAbstractSlider::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDialCall12 call = reinterpret_cast<CuteQDialCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractSlider::changeEvent(e);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDialCall13 call = reinterpret_cast<CuteQDialCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDialCall14 call = reinterpret_cast<CuteQDialCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDialCall15 call = reinterpret_cast<CuteQDialCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDialCall16 call = reinterpret_cast<CuteQDialCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQDialCall17 call = reinterpret_cast<CuteQDialCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDialCall18 call = reinterpret_cast<CuteQDialCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDialCall19 call = reinterpret_cast<CuteQDialCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDialCall20 call = reinterpret_cast<CuteQDialCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDialCall21 call = reinterpret_cast<CuteQDialCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDialCall22 call = reinterpret_cast<CuteQDialCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDialCall23 call = reinterpret_cast<CuteQDialCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDialCall24 call = reinterpret_cast<CuteQDialCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDialCall25 call = reinterpret_cast<CuteQDialCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDialCall26 call = reinterpret_cast<CuteQDialCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDialCall27 call = reinterpret_cast<CuteQDialCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDialCall28 call = reinterpret_cast<CuteQDialCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDialCall29 call = reinterpret_cast<CuteQDialCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDialCall30 call = reinterpret_cast<CuteQDialCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDialCall31 call = reinterpret_cast<CuteQDialCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDialCall32 call = reinterpret_cast<CuteQDialCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDialCall33 call = reinterpret_cast<CuteQDialCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDialCall34 call = reinterpret_cast<CuteQDialCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQDialCall35 call = reinterpret_cast<CuteQDialCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDialCall36 call = reinterpret_cast<CuteQDialCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDialCall37 call = reinterpret_cast<CuteQDialCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDialCall38 call = reinterpret_cast<CuteQDialCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDialCall39 call = reinterpret_cast<CuteQDialCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQDialCall40 call = reinterpret_cast<CuteQDialCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDialCall41 call = reinterpret_cast<CuteQDialCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDialCall42 call = reinterpret_cast<CuteQDialCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDialCall43 call = reinterpret_cast<CuteQDialCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDialCall44 call = reinterpret_cast<CuteQDialCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDialCall45 call = reinterpret_cast<CuteQDialCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDialCall46 call = reinterpret_cast<CuteQDialCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QDial10metaObjectEv(const QDial *self) {
  return self->metaObject();
}

//  QString QDial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QDial2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDial::tr(s, c, n));
}

//  QDial::QDial(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDial *ritual_ZN5QDialC1EP7QWidget(QWidget *parent) {
  return new CuteQDial(parent);
}

//  QDial::~QDial()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDialD1Ev(QDial *self) {
  delete self;
}

//  bool QDial::wrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDial8wrappingEv(const QDial *self) {
  return self->wrapping();
}

//  int QDial::notchSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDial9notchSizeEv(const QDial *self) {
  return self->notchSize();
}

//  void QDial::setNotchTarget(double target)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDial14setNotchTargetEd(QDial *self, double target) {
  self->setNotchTarget(target);
}

//  qreal QDial::notchTarget() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK5QDial11notchTargetEv(const QDial *self) {
  return self->notchTarget();
}

//  bool QDial::notchesVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDial14notchesVisibleEv(const QDial *self) {
  return self->notchesVisible();
}

//  QSize QDial::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QDial8sizeHintEv(const QDial *self) {
  return new QSize(self->sizeHint());
}

//  QSize QDial::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QDial15minimumSizeHintEv(const QDial *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QDial::setNotchesVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDial17setNotchesVisibleEb(QDial *self, bool visible) {
  self->setNotchesVisible(visible);
}

//  void QDial::setWrapping(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDial11setWrappingEb(QDial *self, bool on) {
  self->setWrapping(on);
}

//  a Python function taken by a CuteQDial, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDial(QDial *self, const char *key, void *call) {
  return static_cast<CuteQDial *>(self)->take(key, call);
}

//  QSize QDial::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK5QDial8sizeHintEv(const QDial *self) {
  return new QSize(self->QDial::sizeHint());
}

//  QSize QDial::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK5QDial15minimumSizeHintEv(const QDial *self) {
  return new QSize(self->QDial::minimumSizeHint());
}

//  bool QDial::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QDial5eventEP6QEvent(QDial *self, QEvent *e) {
  return static_cast<OwnQDial *>(self)->OwnQDial::event(e);
}

//  void QDial::resizeEvent(QResizeEvent *re)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QDial11resizeEventEP12QResizeEvent(
    QDial *self,
    QResizeEvent *re) {
  static_cast<OwnQDial *>(self)->OwnQDial::resizeEvent(re);
}

//  void QDial::paintEvent(QPaintEvent *pe)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QDial10paintEventEP11QPaintEvent(
    QDial *self,
    QPaintEvent *pe) {
  static_cast<OwnQDial *>(self)->OwnQDial::paintEvent(pe);
}

//  void QDial::mousePressEvent(QMouseEvent *me)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QDial15mousePressEventEP11QMouseEvent(
    QDial *self,
    QMouseEvent *me) {
  static_cast<OwnQDial *>(self)->OwnQDial::mousePressEvent(me);
}

//  void QDial::mouseReleaseEvent(QMouseEvent *me)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QDial17mouseReleaseEventEP11QMouseEvent(
    QDial *self,
    QMouseEvent *me) {
  static_cast<OwnQDial *>(self)->OwnQDial::mouseReleaseEvent(me);
}

//  void QDial::mouseMoveEvent(QMouseEvent *me)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QDial14mouseMoveEventEP11QMouseEvent(
    QDial *self,
    QMouseEvent *me) {
  static_cast<OwnQDial *>(self)->OwnQDial::mouseMoveEvent(me);
}

//  void QDial::initStyleOption(QStyleOptionSlider *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK5QDial15initStyleOptionEP18QStyleOptionSlider(
    const QDial *self,
    QStyleOptionSlider *option) {
  static_cast<const OwnQDial *>(self)->OwnQDial::initStyleOption(option);
}
