//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDialog : QDialog {
  using QDialog::keyPressEvent;
  using QDialog::closeEvent;
  using QDialog::showEvent;
  using QDialog::resizeEvent;
  using QDialog::contextMenuEvent;
  using QDialog::eventFilter;
};

//  A QDialog that Python can take functions over in. Every QDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDialogCall0)(const void *, bool, int *);
typedef const QSize * (*CuteQDialogCall1)(const void *, int *);
typedef const QSize * (*CuteQDialogCall2)(const void *, int *);
typedef void (*CuteQDialogCall3)(const void *, int *);
typedef int (*CuteQDialogCall4)(const void *, int *);
typedef void (*CuteQDialogCall5)(const void *, int, int *);
typedef void (*CuteQDialogCall6)(const void *, int *);
typedef void (*CuteQDialogCall7)(const void *, int *);
typedef void (*CuteQDialogCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDialogCall9)(const void *, QCloseEvent *, int *);
typedef void (*CuteQDialogCall10)(const void *, QShowEvent *, int *);
typedef void (*CuteQDialogCall11)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDialogCall12)(const void *, QContextMenuEvent *, int *);
typedef bool (*CuteQDialogCall13)(const void *, QObject *, QEvent *, int *);
typedef int (*CuteQDialogCall14)(const void *, int *);
typedef int (*CuteQDialogCall15)(const void *, int, int *);
typedef bool (*CuteQDialogCall16)(const void *, int *);
typedef void * (*CuteQDialogCall17)(const void *, int *);
typedef bool (*CuteQDialogCall18)(const void *, QEvent *, int *);
typedef void (*CuteQDialogCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogCall23)(const void *, QWheelEvent *, int *);
typedef void (*CuteQDialogCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDialogCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDialogCall27)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDialogCall28)(const void *, QEvent *, int *);
typedef void (*CuteQDialogCall29)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDialogCall30)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDialogCall31)(const void *, QTabletEvent *, int *);
typedef void (*CuteQDialogCall32)(const void *, QActionEvent *, int *);
typedef void (*CuteQDialogCall33)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQDialogCall34)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQDialogCall35)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQDialogCall36)(const void *, QDropEvent *, int *);
typedef void (*CuteQDialogCall37)(const void *, QHideEvent *, int *);
typedef void (*CuteQDialogCall38)(const void *, QEvent *, int *);
typedef int (*CuteQDialogCall39)(const void *, int, int *);
typedef void (*CuteQDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQDialogCall42)(const void *, int *);
typedef void (*CuteQDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDialogCall44)(const void *, int, int *);
typedef bool (*CuteQDialogCall45)(const void *, bool, int *);
typedef void (*CuteQDialogCall46)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDialogCall47)(const void *, QChildEvent *, int *);
typedef void (*CuteQDialogCall48)(const void *, QEvent *, int *);
typedef void (*CuteQDialogCall49)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDialogCall50)(const void *, const QMetaMethod *, int *);
class CuteQDialog : public QDialog {
public:
  using QDialog::QDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
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
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
    return false;
  }

  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDialogCall0 call = reinterpret_cast<CuteQDialogCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }

  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDialogCall1 call = reinterpret_cast<CuteQDialogCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }

  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDialogCall2 call = reinterpret_cast<CuteQDialogCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }

  //  void QDialog::open()
  void open() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDialogCall3 call = reinterpret_cast<CuteQDialogCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }

  //  int QDialog::exec()
  int exec() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDialogCall4 call = reinterpret_cast<CuteQDialogCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }

  //  void QDialog::done(int a0)
  void done(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDialogCall5 call = reinterpret_cast<CuteQDialogCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::done(a0);
  }

  //  void QDialog::accept()
  void accept() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDialogCall6 call = reinterpret_cast<CuteQDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }

  //  void QDialog::reject()
  void reject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDialogCall7 call = reinterpret_cast<CuteQDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }

  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDialogCall8 call = reinterpret_cast<CuteQDialogCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }

  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDialogCall9 call = reinterpret_cast<CuteQDialogCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }

  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDialogCall10 call = reinterpret_cast<CuteQDialogCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }

  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDialogCall11 call = reinterpret_cast<CuteQDialogCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::resizeEvent(a0);
  }

  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDialogCall12 call = reinterpret_cast<CuteQDialogCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }

  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDialogCall13 call = reinterpret_cast<CuteQDialogCall13>(taken[13]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDialogCall14 call = reinterpret_cast<CuteQDialogCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDialogCall15 call = reinterpret_cast<CuteQDialogCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDialogCall16 call = reinterpret_cast<CuteQDialogCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQDialogCall17 call = reinterpret_cast<CuteQDialogCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDialogCall18 call = reinterpret_cast<CuteQDialogCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDialogCall19 call = reinterpret_cast<CuteQDialogCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDialogCall20 call = reinterpret_cast<CuteQDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDialogCall21 call = reinterpret_cast<CuteQDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDialogCall22 call = reinterpret_cast<CuteQDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDialogCall23 call = reinterpret_cast<CuteQDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDialogCall24 call = reinterpret_cast<CuteQDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDialogCall25 call = reinterpret_cast<CuteQDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDialogCall26 call = reinterpret_cast<CuteQDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDialogCall27 call = reinterpret_cast<CuteQDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDialogCall28 call = reinterpret_cast<CuteQDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDialogCall29 call = reinterpret_cast<CuteQDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDialogCall30 call = reinterpret_cast<CuteQDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDialogCall31 call = reinterpret_cast<CuteQDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDialogCall32 call = reinterpret_cast<CuteQDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDialogCall33 call = reinterpret_cast<CuteQDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDialogCall34 call = reinterpret_cast<CuteQDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDialogCall35 call = reinterpret_cast<CuteQDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDialogCall36 call = reinterpret_cast<CuteQDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDialogCall37 call = reinterpret_cast<CuteQDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDialogCall38 call = reinterpret_cast<CuteQDialogCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDialogCall39 call = reinterpret_cast<CuteQDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQDialogCall40 call = reinterpret_cast<CuteQDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQDialogCall41 call = reinterpret_cast<CuteQDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQDialogCall42 call = reinterpret_cast<CuteQDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDialogCall43 call = reinterpret_cast<CuteQDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQDialogCall44 call = reinterpret_cast<CuteQDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDialogCall45 call = reinterpret_cast<CuteQDialogCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDialogCall46 call = reinterpret_cast<CuteQDialogCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDialogCall47 call = reinterpret_cast<CuteQDialogCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQDialogCall48 call = reinterpret_cast<CuteQDialogCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQDialogCall49 call = reinterpret_cast<CuteQDialogCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQDialogCall50 call = reinterpret_cast<CuteQDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QDialog10metaObjectEv(const QDialog *self) {
  return self->metaObject();
}

//  QString QDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QDialog2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDialog::tr(s, c, n));
}

//  QDialog::QDialog(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZN7QDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQDialog(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QDialog::~QDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialogD1Ev(QDialog *self) {
  delete self;
}

//  int QDialog::result() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QDialog6resultEv(const QDialog *self) {
  return self->result();
}

//  void QDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog10setVisibleEb(QDialog *self, bool visible) {
  self->setVisible(visible);
}

//  QSize QDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QDialog8sizeHintEv(const QDialog *self) {
  return new QSize(self->sizeHint());
}

//  QSize QDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QDialog15minimumSizeHintEv(const QDialog *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QDialog::setSizeGripEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog18setSizeGripEnabledEb(QDialog *self, bool a0) {
  self->setSizeGripEnabled(a0);
}

//  bool QDialog::isSizeGripEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QDialog17isSizeGripEnabledEv(const QDialog *self) {
  return self->isSizeGripEnabled();
}

//  void QDialog::setModal(bool modal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog8setModalEb(QDialog *self, bool modal) {
  self->setModal(modal);
}

//  void QDialog::setResult(int r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog9setResultEi(QDialog *self, int r) {
  self->setResult(r);
}

//  void QDialog::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog4openEv(QDialog *self) {
  self->open();
}

//  int QDialog::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QDialog4execEv(QDialog *self) {
  return self->exec();
}

//  void QDialog::done(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog4doneEi(QDialog *self, int a0) {
  self->done(a0);
}

//  void QDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog6acceptEv(QDialog *self) {
  self->accept();
}

//  void QDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QDialog6rejectEv(QDialog *self) {
  self->reject();
}

//  a Python function taken by a CuteQDialog, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDialog(QDialog *self, const char *key, void *call) {
  return static_cast<CuteQDialog *>(self)->take(key, call);
}

//  void QDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog10setVisibleEb(QDialog *self, bool visible) {
  self->QDialog::setVisible(visible);
}

//  QSize QDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QDialog8sizeHintEv(const QDialog *self) {
  return new QSize(self->QDialog::sizeHint());
}

//  QSize QDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QDialog15minimumSizeHintEv(const QDialog *self) {
  return new QSize(self->QDialog::minimumSizeHint());
}

//  void QDialog::open()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog4openEv(QDialog *self) {
  self->QDialog::open();
}

//  int QDialog::exec()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN7QDialog4execEv(QDialog *self) {
  return self->QDialog::exec();
}

//  void QDialog::done(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog4doneEi(QDialog *self, int a0) {
  self->QDialog::done(a0);
}

//  void QDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog6acceptEv(QDialog *self) {
  self->QDialog::accept();
}

//  void QDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog6rejectEv(QDialog *self) {
  self->QDialog::reject();
}

//  void QDialog::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog13keyPressEventEP9QKeyEvent(
    QDialog *self,
    QKeyEvent *a0) {
  static_cast<OwnQDialog *>(self)->OwnQDialog::keyPressEvent(a0);
}

//  void QDialog::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog10closeEventEP11QCloseEvent(
    QDialog *self,
    QCloseEvent *a0) {
  static_cast<OwnQDialog *>(self)->OwnQDialog::closeEvent(a0);
}

//  void QDialog::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog9showEventEP10QShowEvent(
    QDialog *self,
    QShowEvent *a0) {
  static_cast<OwnQDialog *>(self)->OwnQDialog::showEvent(a0);
}

//  void QDialog::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog11resizeEventEP12QResizeEvent(
    QDialog *self,
    QResizeEvent *a0) {
  static_cast<OwnQDialog *>(self)->OwnQDialog::resizeEvent(a0);
}

//  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QDialog16contextMenuEventEP17QContextMenuEvent(
    QDialog *self,
    QContextMenuEvent *a0) {
  static_cast<OwnQDialog *>(self)->OwnQDialog::contextMenuEvent(a0);
}

//  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QDialog11eventFilterEP7QObjectP6QEvent(
    QDialog *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQDialog *>(self)->OwnQDialog::eventFilter(a0, a1);
}
