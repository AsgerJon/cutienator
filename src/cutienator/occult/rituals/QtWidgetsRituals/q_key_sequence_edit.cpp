//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qkeysequenceedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qkeysequenceedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QKeySequenceEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQKeySequenceEdit : QKeySequenceEdit {
  using QKeySequenceEdit::event;
  using QKeySequenceEdit::keyPressEvent;
  using QKeySequenceEdit::keyReleaseEvent;
  using QKeySequenceEdit::timerEvent;
  using QKeySequenceEdit::focusOutEvent;
};

//  A QKeySequenceEdit that Python can take functions over in. Every QKeySequenceEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQKeySequenceEditCall0)(const void *, QEvent *, int *);
typedef void (*CuteQKeySequenceEditCall1)(const void *, QKeyEvent *, int *);
typedef void (*CuteQKeySequenceEditCall2)(const void *, QKeyEvent *, int *);
typedef void (*CuteQKeySequenceEditCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQKeySequenceEditCall4)(const void *, QFocusEvent *, int *);
typedef int (*CuteQKeySequenceEditCall5)(const void *, int *);
typedef void (*CuteQKeySequenceEditCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQKeySequenceEditCall7)(const void *, int *);
typedef const QSize * (*CuteQKeySequenceEditCall8)(const void *, int *);
typedef int (*CuteQKeySequenceEditCall9)(const void *, int, int *);
typedef bool (*CuteQKeySequenceEditCall10)(const void *, int *);
typedef void * (*CuteQKeySequenceEditCall11)(const void *, int *);
typedef void (*CuteQKeySequenceEditCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQKeySequenceEditCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQKeySequenceEditCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQKeySequenceEditCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQKeySequenceEditCall16)(const void *, QWheelEvent *, int *);
typedef void (*CuteQKeySequenceEditCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQKeySequenceEditCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQKeySequenceEditCall19)(const void *, QEvent *, int *);
typedef void (*CuteQKeySequenceEditCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQKeySequenceEditCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQKeySequenceEditCall22)(const void *, QResizeEvent *, int *);
typedef void (*CuteQKeySequenceEditCall23)(const void *, QCloseEvent *, int *);
typedef void (*CuteQKeySequenceEditCall24)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQKeySequenceEditCall25)(const void *, QTabletEvent *, int *);
typedef void (*CuteQKeySequenceEditCall26)(const void *, QActionEvent *, int *);
typedef void (*CuteQKeySequenceEditCall27)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQKeySequenceEditCall28)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQKeySequenceEditCall29)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQKeySequenceEditCall30)(const void *, QDropEvent *, int *);
typedef void (*CuteQKeySequenceEditCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQKeySequenceEditCall32)(const void *, QHideEvent *, int *);
typedef void (*CuteQKeySequenceEditCall33)(const void *, QEvent *, int *);
typedef int (*CuteQKeySequenceEditCall34)(const void *, int, int *);
typedef void (*CuteQKeySequenceEditCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQKeySequenceEditCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQKeySequenceEditCall37)(const void *, int *);
typedef void (*CuteQKeySequenceEditCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQKeySequenceEditCall39)(const void *, int, int *);
typedef bool (*CuteQKeySequenceEditCall40)(const void *, bool, int *);
typedef bool (*CuteQKeySequenceEditCall41)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQKeySequenceEditCall42)(const void *, QChildEvent *, int *);
typedef void (*CuteQKeySequenceEditCall43)(const void *, QEvent *, int *);
typedef void (*CuteQKeySequenceEditCall44)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQKeySequenceEditCall45)(const void *, const QMetaMethod *, int *);
class CuteQKeySequenceEdit : public QKeySequenceEdit {
public:
  using QKeySequenceEdit::QKeySequenceEdit;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    return false;
  }

  //  bool QKeySequenceEdit::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQKeySequenceEditCall0 call = reinterpret_cast<CuteQKeySequenceEditCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QKeySequenceEdit::event(a0);
  }

  //  void QKeySequenceEdit::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQKeySequenceEditCall1 call = reinterpret_cast<CuteQKeySequenceEditCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QKeySequenceEdit::keyPressEvent(a0);
  }

  //  void QKeySequenceEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQKeySequenceEditCall2 call = reinterpret_cast<CuteQKeySequenceEditCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QKeySequenceEdit::keyReleaseEvent(a0);
  }

  //  void QKeySequenceEdit::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQKeySequenceEditCall3 call = reinterpret_cast<CuteQKeySequenceEditCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QKeySequenceEdit::timerEvent(a0);
  }

  //  void QKeySequenceEdit::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQKeySequenceEditCall4 call = reinterpret_cast<CuteQKeySequenceEditCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QKeySequenceEdit::focusOutEvent(a0);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQKeySequenceEditCall5 call = reinterpret_cast<CuteQKeySequenceEditCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQKeySequenceEditCall6 call = reinterpret_cast<CuteQKeySequenceEditCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQKeySequenceEditCall7 call = reinterpret_cast<CuteQKeySequenceEditCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQKeySequenceEditCall8 call = reinterpret_cast<CuteQKeySequenceEditCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQKeySequenceEditCall9 call = reinterpret_cast<CuteQKeySequenceEditCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQKeySequenceEditCall10 call = reinterpret_cast<CuteQKeySequenceEditCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQKeySequenceEditCall11 call = reinterpret_cast<CuteQKeySequenceEditCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQKeySequenceEditCall12 call = reinterpret_cast<CuteQKeySequenceEditCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQKeySequenceEditCall13 call = reinterpret_cast<CuteQKeySequenceEditCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQKeySequenceEditCall14 call = reinterpret_cast<CuteQKeySequenceEditCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQKeySequenceEditCall15 call = reinterpret_cast<CuteQKeySequenceEditCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQKeySequenceEditCall16 call = reinterpret_cast<CuteQKeySequenceEditCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQKeySequenceEditCall17 call = reinterpret_cast<CuteQKeySequenceEditCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQKeySequenceEditCall18 call = reinterpret_cast<CuteQKeySequenceEditCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQKeySequenceEditCall19 call = reinterpret_cast<CuteQKeySequenceEditCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQKeySequenceEditCall20 call = reinterpret_cast<CuteQKeySequenceEditCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQKeySequenceEditCall21 call = reinterpret_cast<CuteQKeySequenceEditCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQKeySequenceEditCall22 call = reinterpret_cast<CuteQKeySequenceEditCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQKeySequenceEditCall23 call = reinterpret_cast<CuteQKeySequenceEditCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQKeySequenceEditCall24 call = reinterpret_cast<CuteQKeySequenceEditCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQKeySequenceEditCall25 call = reinterpret_cast<CuteQKeySequenceEditCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQKeySequenceEditCall26 call = reinterpret_cast<CuteQKeySequenceEditCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQKeySequenceEditCall27 call = reinterpret_cast<CuteQKeySequenceEditCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQKeySequenceEditCall28 call = reinterpret_cast<CuteQKeySequenceEditCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQKeySequenceEditCall29 call = reinterpret_cast<CuteQKeySequenceEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQKeySequenceEditCall30 call = reinterpret_cast<CuteQKeySequenceEditCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQKeySequenceEditCall31 call = reinterpret_cast<CuteQKeySequenceEditCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQKeySequenceEditCall32 call = reinterpret_cast<CuteQKeySequenceEditCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQKeySequenceEditCall33 call = reinterpret_cast<CuteQKeySequenceEditCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQKeySequenceEditCall34 call = reinterpret_cast<CuteQKeySequenceEditCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQKeySequenceEditCall35 call = reinterpret_cast<CuteQKeySequenceEditCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQKeySequenceEditCall36 call = reinterpret_cast<CuteQKeySequenceEditCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQKeySequenceEditCall37 call = reinterpret_cast<CuteQKeySequenceEditCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQKeySequenceEditCall38 call = reinterpret_cast<CuteQKeySequenceEditCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQKeySequenceEditCall39 call = reinterpret_cast<CuteQKeySequenceEditCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQKeySequenceEditCall40 call = reinterpret_cast<CuteQKeySequenceEditCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQKeySequenceEditCall41 call = reinterpret_cast<CuteQKeySequenceEditCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQKeySequenceEditCall42 call = reinterpret_cast<CuteQKeySequenceEditCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQKeySequenceEditCall43 call = reinterpret_cast<CuteQKeySequenceEditCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQKeySequenceEditCall44 call = reinterpret_cast<CuteQKeySequenceEditCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQKeySequenceEditCall45 call = reinterpret_cast<CuteQKeySequenceEditCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QKeySequenceEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QKeySequenceEdit10metaObjectEv(
    const QKeySequenceEdit *self) {
  return self->metaObject();
}

//  QString QKeySequenceEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QKeySequenceEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QKeySequenceEdit::tr(s, c, n));
}

//  QKeySequenceEdit::QKeySequenceEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QKeySequenceEdit *ritual_ZN16QKeySequenceEditC1EP7QWidget(QWidget *parent) {
  return new CuteQKeySequenceEdit(parent);
}

//  QKeySequenceEdit::QKeySequenceEdit(const QKeySequence &keySequence,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QKeySequenceEdit *ritual_ZN16QKeySequenceEditC1ERK12QKeySequenceP7QWidget(
    const QKeySequence *keySequence,
    QWidget *parent) {
  return new CuteQKeySequenceEdit(*keySequence, parent);
}

//  QKeySequenceEdit::~QKeySequenceEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEditD1Ev(QKeySequenceEdit *self) {
  delete self;
}

//  QKeySequence QKeySequenceEdit::keySequence() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK16QKeySequenceEdit11keySequenceEv(
    const QKeySequenceEdit *self) {
  return new QKeySequence(self->keySequence());
}

//  qsizetype QKeySequenceEdit::maximumSequenceLength() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QKeySequenceEdit21maximumSequenceLengthEv(
    const QKeySequenceEdit *self) {
  return self->maximumSequenceLength();
}

//  void QKeySequenceEdit::setClearButtonEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit21setClearButtonEnabledEb(
    QKeySequenceEdit *self,
    bool enable) {
  self->setClearButtonEnabled(enable);
}

//  bool QKeySequenceEdit::isClearButtonEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QKeySequenceEdit20isClearButtonEnabledEv(
    const QKeySequenceEdit *self) {
  return self->isClearButtonEnabled();
}

//  void QKeySequenceEdit::setFinishingKeyCombinations(const
//      QList<QKeyCombination> &finishingKeyCombinations)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit27setFinishingKeyCombinationsERK5QListI15QKeyCombinationE(
    QKeySequenceEdit *self,
    const QList<QKeyCombination> *finishingKeyCombinations) {
  self->setFinishingKeyCombinations(*finishingKeyCombinations);
}

//  QList<QKeyCombination> QKeySequenceEdit::finishingKeyCombinations() const
extern "C" Q_DECL_EXPORT
QList<QKeyCombination> *ritual_ZNK16QKeySequenceEdit24finishingKeyCombinationsEv(
    const QKeySequenceEdit *self) {
  return new QList<QKeyCombination>(self->finishingKeyCombinations());
}

//  void QKeySequenceEdit::setKeySequence(const QKeySequence &keySequence)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit14setKeySequenceERK12QKeySequence(
    QKeySequenceEdit *self,
    const QKeySequence *keySequence) {
  self->setKeySequence(*keySequence);
}

//  void QKeySequenceEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit5clearEv(QKeySequenceEdit *self) {
  self->clear();
}

//  void QKeySequenceEdit::setMaximumSequenceLength(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit24setMaximumSequenceLengthEx(
    QKeySequenceEdit *self,
    qsizetype count) {
  self->setMaximumSequenceLength(count);
}

//  bool QKeySequenceEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QKeySequenceEdit5eventEP6QEvent(
    QKeySequenceEdit *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QKeySequenceEdit::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit13keyPressEventEP9QKeyEvent(
    QKeySequenceEdit *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QKeySequenceEdit::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit15keyReleaseEventEP9QKeyEvent(
    QKeySequenceEdit *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QKeySequenceEdit::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit10timerEventEP11QTimerEvent(
    QKeySequenceEdit *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QKeySequenceEdit::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QKeySequenceEdit13focusOutEventEP11QFocusEvent(
    QKeySequenceEdit *self,
    QFocusEvent *a0) {
  self->focusOutEvent(a0);
}

//  QKeySequenceEditPrivate *QKeySequenceEdit::d_func()
extern "C" Q_DECL_EXPORT
QKeySequenceEditPrivate *ritual_ZN16QKeySequenceEdit6d_funcEv(
    QKeySequenceEdit *self) {
  return self->d_func();
}

//  const QKeySequenceEditPrivate *QKeySequenceEdit::d_func() const
extern "C" Q_DECL_EXPORT
const QKeySequenceEditPrivate *ritual_ZNK16QKeySequenceEdit6d_funcEv(
    const QKeySequenceEdit *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQKeySequenceEdit, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKeySequenceEdit(
    QKeySequenceEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQKeySequenceEdit *>(self)->take(key, call);
}

//  bool QKeySequenceEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QKeySequenceEdit5eventEP6QEvent(
    QKeySequenceEdit *self,
    QEvent *a0) {
  return static_cast<OwnQKeySequenceEdit *>(self)->OwnQKeySequenceEdit::event(
      a0);
}

//  void QKeySequenceEdit::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QKeySequenceEdit13keyPressEventEP9QKeyEvent(
    QKeySequenceEdit *self,
    QKeyEvent *a0) {
  static_cast<OwnQKeySequenceEdit *>(self)->OwnQKeySequenceEdit::keyPressEvent(
      a0);
}

//  void QKeySequenceEdit::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QKeySequenceEdit15keyReleaseEventEP9QKeyEvent(
    QKeySequenceEdit *self,
    QKeyEvent *a0) {
  static_cast<OwnQKeySequenceEdit *>(self)->OwnQKeySequenceEdit::keyReleaseEvent(
      a0);
}

//  void QKeySequenceEdit::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QKeySequenceEdit10timerEventEP11QTimerEvent(
    QKeySequenceEdit *self,
    QTimerEvent *a0) {
  static_cast<OwnQKeySequenceEdit *>(self)->OwnQKeySequenceEdit::timerEvent(
      a0);
}

//  void QKeySequenceEdit::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QKeySequenceEdit13focusOutEventEP11QFocusEvent(
    QKeySequenceEdit *self,
    QFocusEvent *a0) {
  static_cast<OwnQKeySequenceEdit *>(self)->OwnQKeySequenceEdit::focusOutEvent(
      a0);
}
