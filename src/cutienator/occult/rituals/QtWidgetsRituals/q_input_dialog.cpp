//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qinputdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(inputdialog)
#if QT_CONFIG(inputdialog)
#include <QtWidgets/qinputdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QInputDialog that Python can take functions over in. Every QInputDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(inputdialog)
typedef const QSize * (*CuteQInputDialogCall0)(const void *, int *);
#endif  // QT_CONFIG(inputdialog)
#if QT_CONFIG(inputdialog)
typedef const QSize * (*CuteQInputDialogCall1)(const void *, int *);
#endif  // QT_CONFIG(inputdialog)
#if QT_CONFIG(inputdialog)
typedef void (*CuteQInputDialogCall2)(const void *, bool, int *);
#endif  // QT_CONFIG(inputdialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(inputdialog)
typedef void (*CuteQInputDialogCall3)(const void *, int, int *);
#endif  // QT_CONFIG(inputdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQInputDialogCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall9)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall10)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall11)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*CuteQInputDialogCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*CuteQInputDialogCall13)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQInputDialogCall14)(const void *, int *);
typedef int (*CuteQInputDialogCall15)(const void *, int, int *);
typedef bool (*CuteQInputDialogCall16)(const void *, int *);
typedef void * (*CuteQInputDialogCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInputDialogCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDialogCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQInputDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQInputDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQInputDialogCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQInputDialogCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQInputDialogCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQInputDialogCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQInputDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQInputDialogCall27)(const void *, QEnterEvent *, int *);
typedef void (*CuteQInputDialogCall28)(const void *, QEvent *, int *);
typedef void (*CuteQInputDialogCall29)(const void *, QPaintEvent *, int *);
typedef void (*CuteQInputDialogCall30)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQInputDialogCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQInputDialogCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQInputDialogCall33)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQInputDialogCall34)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQInputDialogCall35)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQInputDialogCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQInputDialogCall37)(const void *, QHideEvent *, int *);
typedef void (*CuteQInputDialogCall38)(const void *, QEvent *, int *);
typedef int (*CuteQInputDialogCall39)(const void *, int, int *);
typedef void (*CuteQInputDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQInputDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQInputDialogCall42)(const void *, int *);
typedef void (*CuteQInputDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQInputDialogCall44)(const void *, int, int *);
typedef bool (*CuteQInputDialogCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDialogCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDialogCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDialogCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDialogCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInputDialogCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQInputDialog : public QInputDialog {
public:
  using QInputDialog::QInputDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(inputdialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(inputdialog)
#if QT_CONFIG(inputdialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(inputdialog)
#if QT_CONFIG(inputdialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(inputdialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(inputdialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(inputdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(inputdialog)
  //  QSize QInputDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQInputDialogCall0 call = reinterpret_cast<CuteQInputDialogCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QInputDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(inputdialog)

#if QT_CONFIG(inputdialog)
  //  QSize QInputDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQInputDialogCall1 call = reinterpret_cast<CuteQInputDialogCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QInputDialog::sizeHint();
  }
#endif  // QT_CONFIG(inputdialog)

#if QT_CONFIG(inputdialog)
  //  void QInputDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQInputDialogCall2 call = reinterpret_cast<CuteQInputDialogCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QInputDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(inputdialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(inputdialog)
  //  void QInputDialog::done(int result)
  void done(int result) override {
    if (taken[3]) {
      int handled = 0;
      CuteQInputDialogCall3 call = reinterpret_cast<CuteQInputDialogCall3>(taken[3]);
      call(this, result, &handled);
      if (handled) return;
    }
    QInputDialog::done(result);
  }
#endif  // QT_CONFIG(inputdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[4]) {
      int handled = 0;
      CuteQInputDialogCall4 call = reinterpret_cast<CuteQInputDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[5]) {
      int handled = 0;
      CuteQInputDialogCall5 call = reinterpret_cast<CuteQInputDialogCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::accept()
  void accept() override {
    if (taken[6]) {
      int handled = 0;
      CuteQInputDialogCall6 call = reinterpret_cast<CuteQInputDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQInputDialogCall7 call = reinterpret_cast<CuteQInputDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQInputDialogCall8 call = reinterpret_cast<CuteQInputDialogCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQInputDialogCall9 call = reinterpret_cast<CuteQInputDialogCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQInputDialogCall10 call = reinterpret_cast<CuteQInputDialogCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQInputDialogCall11 call = reinterpret_cast<CuteQInputDialogCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::resizeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQInputDialogCall12 call = reinterpret_cast<CuteQInputDialogCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[13]) {
      int handled = 0;
      CuteQInputDialogCall13 call = reinterpret_cast<CuteQInputDialogCall13>(taken[13]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQInputDialogCall14 call = reinterpret_cast<CuteQInputDialogCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQInputDialogCall15 call = reinterpret_cast<CuteQInputDialogCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQInputDialogCall16 call = reinterpret_cast<CuteQInputDialogCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQInputDialogCall17 call = reinterpret_cast<CuteQInputDialogCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQInputDialogCall18 call = reinterpret_cast<CuteQInputDialogCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQInputDialogCall19 call = reinterpret_cast<CuteQInputDialogCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQInputDialogCall20 call = reinterpret_cast<CuteQInputDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQInputDialogCall21 call = reinterpret_cast<CuteQInputDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQInputDialogCall22 call = reinterpret_cast<CuteQInputDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQInputDialogCall23 call = reinterpret_cast<CuteQInputDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQInputDialogCall24 call = reinterpret_cast<CuteQInputDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQInputDialogCall25 call = reinterpret_cast<CuteQInputDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQInputDialogCall26 call = reinterpret_cast<CuteQInputDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQInputDialogCall27 call = reinterpret_cast<CuteQInputDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQInputDialogCall28 call = reinterpret_cast<CuteQInputDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQInputDialogCall29 call = reinterpret_cast<CuteQInputDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQInputDialogCall30 call = reinterpret_cast<CuteQInputDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQInputDialogCall31 call = reinterpret_cast<CuteQInputDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQInputDialogCall32 call = reinterpret_cast<CuteQInputDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQInputDialogCall33 call = reinterpret_cast<CuteQInputDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQInputDialogCall34 call = reinterpret_cast<CuteQInputDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQInputDialogCall35 call = reinterpret_cast<CuteQInputDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQInputDialogCall36 call = reinterpret_cast<CuteQInputDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQInputDialogCall37 call = reinterpret_cast<CuteQInputDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQInputDialogCall38 call = reinterpret_cast<CuteQInputDialogCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQInputDialogCall39 call = reinterpret_cast<CuteQInputDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQInputDialogCall40 call = reinterpret_cast<CuteQInputDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQInputDialogCall41 call = reinterpret_cast<CuteQInputDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQInputDialogCall42 call = reinterpret_cast<CuteQInputDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQInputDialogCall43 call = reinterpret_cast<CuteQInputDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQInputDialogCall44 call = reinterpret_cast<CuteQInputDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQInputDialogCall45 call = reinterpret_cast<CuteQInputDialogCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQInputDialogCall46 call = reinterpret_cast<CuteQInputDialogCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQInputDialogCall47 call = reinterpret_cast<CuteQInputDialogCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQInputDialogCall48 call = reinterpret_cast<CuteQInputDialogCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQInputDialogCall49 call = reinterpret_cast<CuteQInputDialogCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQInputDialogCall50 call = reinterpret_cast<CuteQInputDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QInputDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QInputDialog10metaObjectEv(
    const QInputDialog *self) {
  return self->metaObject();
}

//  QString QInputDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputDialog::tr(s, c, n));
}

//  QInputDialog::QInputDialog(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QInputDialog *ritual_ZN12QInputDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQInputDialog(
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QInputDialog::~QInputDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialogD1Ev(QInputDialog *self) {
  delete self;
}

//  void QInputDialog::setInputMode(InputMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog12setInputModeENS_9InputModeE(
    QInputDialog *self,
    QInputDialog::InputMode mode) {
  self->setInputMode(mode);
}

//  InputMode QInputDialog::inputMode() const
extern "C" Q_DECL_EXPORT
QInputDialog::InputMode ritual_ZNK12QInputDialog9inputModeEv(
    const QInputDialog *self) {
  return self->inputMode();
}

//  void QInputDialog::setLabelText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog12setLabelTextERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setLabelText(*text);
}

//  QString QInputDialog::labelText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog9labelTextEv(const QInputDialog *self) {
  return new QString(self->labelText());
}

//  void QInputDialog::setOption(InputDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog9setOptionENS_17InputDialogOptionEb(
    QInputDialog *self,
    QInputDialog::InputDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QInputDialog::testOption(InputDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputDialog10testOptionENS_17InputDialogOptionE(
    const QInputDialog *self,
    QInputDialog::InputDialogOption option) {
  return self->testOption(option);
}

//  void QInputDialog::setOptions(InputDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog10setOptionsE6QFlagsINS_17InputDialogOptionEE(
    QInputDialog *self,
    int options) {
  self->setOptions(
      QFlags<QInputDialog::InputDialogOption>::fromInt(options));
}

//  InputDialogOptions QInputDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog7optionsEv(const QInputDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QInputDialog::setTextValue(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog12setTextValueERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setTextValue(*text);
}

//  QString QInputDialog::textValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog9textValueEv(const QInputDialog *self) {
  return new QString(self->textValue());
}

//  void QInputDialog::setTextEchoMode(QLineEdit::EchoMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog15setTextEchoModeEN9QLineEdit8EchoModeE(
    QInputDialog *self,
    QLineEdit::EchoMode mode) {
  self->setTextEchoMode(mode);
}

//  QLineEdit::EchoMode QInputDialog::textEchoMode() const
extern "C" Q_DECL_EXPORT
QLineEdit::EchoMode ritual_ZNK12QInputDialog12textEchoModeEv(
    const QInputDialog *self) {
  return self->textEchoMode();
}

//  void QInputDialog::setComboBoxEditable(bool editable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog19setComboBoxEditableEb(
    QInputDialog *self,
    bool editable) {
  self->setComboBoxEditable(editable);
}

//  bool QInputDialog::isComboBoxEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputDialog18isComboBoxEditableEv(
    const QInputDialog *self) {
  return self->isComboBoxEditable();
}

//  void QInputDialog::setComboBoxItems(const QStringList &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog16setComboBoxItemsERK5QListI7QStringE(
    QInputDialog *self,
    const QList<QString> *items) {
  self->setComboBoxItems(*items);
}

//  QStringList QInputDialog::comboBoxItems() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QInputDialog13comboBoxItemsEv(
    const QInputDialog *self) {
  return new QList<QString>(self->comboBoxItems());
}

//  void QInputDialog::setIntValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog11setIntValueEi(QInputDialog *self, int value) {
  self->setIntValue(value);
}

//  int QInputDialog::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog8intValueEv(const QInputDialog *self) {
  return self->intValue();
}

//  void QInputDialog::setIntMinimum(int min)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog13setIntMinimumEi(QInputDialog *self, int min) {
  self->setIntMinimum(min);
}

//  int QInputDialog::intMinimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog10intMinimumEv(const QInputDialog *self) {
  return self->intMinimum();
}

//  void QInputDialog::setIntMaximum(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog13setIntMaximumEi(QInputDialog *self, int max) {
  self->setIntMaximum(max);
}

//  int QInputDialog::intMaximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog10intMaximumEv(const QInputDialog *self) {
  return self->intMaximum();
}

//  void QInputDialog::setIntRange(int min, int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog11setIntRangeEii(
    QInputDialog *self,
    int min,
    int max) {
  self->setIntRange(min, max);
}

//  void QInputDialog::setIntStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog10setIntStepEi(QInputDialog *self, int step) {
  self->setIntStep(step);
}

//  int QInputDialog::intStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog7intStepEv(const QInputDialog *self) {
  return self->intStep();
}

//  void QInputDialog::setDoubleValue(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog14setDoubleValueEd(
    QInputDialog *self,
    double value) {
  self->setDoubleValue(value);
}

//  double QInputDialog::doubleValue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog11doubleValueEv(const QInputDialog *self) {
  return self->doubleValue();
}

//  void QInputDialog::setDoubleMinimum(double min)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog16setDoubleMinimumEd(
    QInputDialog *self,
    double min) {
  self->setDoubleMinimum(min);
}

//  double QInputDialog::doubleMinimum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog13doubleMinimumEv(const QInputDialog *self) {
  return self->doubleMinimum();
}

//  void QInputDialog::setDoubleMaximum(double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog16setDoubleMaximumEd(
    QInputDialog *self,
    double max) {
  self->setDoubleMaximum(max);
}

//  double QInputDialog::doubleMaximum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog13doubleMaximumEv(const QInputDialog *self) {
  return self->doubleMaximum();
}

//  void QInputDialog::setDoubleRange(double min, double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog14setDoubleRangeEdd(
    QInputDialog *self,
    double min,
    double max) {
  self->setDoubleRange(min, max);
}

//  void QInputDialog::setDoubleDecimals(int decimals)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog17setDoubleDecimalsEi(
    QInputDialog *self,
    int decimals) {
  self->setDoubleDecimals(decimals);
}

//  int QInputDialog::doubleDecimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDialog14doubleDecimalsEv(const QInputDialog *self) {
  return self->doubleDecimals();
}

//  void QInputDialog::setOkButtonText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog15setOkButtonTextERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setOkButtonText(*text);
}

//  QString QInputDialog::okButtonText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog12okButtonTextEv(const QInputDialog *self) {
  return new QString(self->okButtonText());
}

//  void QInputDialog::setCancelButtonText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog19setCancelButtonTextERK7QString(
    QInputDialog *self,
    const QString *text) {
  self->setCancelButtonText(*text);
}

//  QString QInputDialog::cancelButtonText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDialog16cancelButtonTextEv(
    const QInputDialog *self) {
  return new QString(self->cancelButtonText());
}

//  void QInputDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog4openEP7QObjectPKc(
    QInputDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  QSize QInputDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QInputDialog15minimumSizeHintEv(
    const QInputDialog *self) {
  return new QSize(self->minimumSizeHint());
}

//  QSize QInputDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QInputDialog8sizeHintEv(const QInputDialog *self) {
  return new QSize(self->sizeHint());
}

//  void QInputDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog10setVisibleEb(
    QInputDialog *self,
    bool visible) {
  self->setVisible(visible);
}

//  QString QInputDialog::getText(QWidget *parent, const QString &title,
//      const QString &label, QLineEdit::EchoMode echo, const QString &text,
//      bool *ok, Qt::WindowFlags flags, Qt::InputMethodHints
//      inputMethodHints)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog7getTextEP7QWidgetRK7QStringS4_N9QLineEdit8EchoModeES4_Pb6QFlagsIN2Qt10WindowTypeEES8_INS9_15InputMethodHintEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    QLineEdit::EchoMode echo,
    const QString *text,
    bool *ok,
    int flags,
    int inputMethodHints) {
  return new QString(
      QInputDialog::getText(
          parent,
          *title,
          *label,
          echo,
          *text,
          ok,
          QFlags<Qt::WindowType>::fromInt(flags),
          QFlags<Qt::InputMethodHint>::fromInt(inputMethodHints)));
}

//  QString QInputDialog::getMultiLineText(QWidget *parent, const QString
//      &title, const QString &label, const QString &text, bool *ok,
//      Qt::WindowFlags flags, Qt::InputMethodHints inputMethodHints)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog16getMultiLineTextEP7QWidgetRK7QStringS4_S4_Pb6QFlagsIN2Qt10WindowTypeEES6_INS7_15InputMethodHintEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    const QString *text,
    bool *ok,
    int flags,
    int inputMethodHints) {
  return new QString(
      QInputDialog::getMultiLineText(
          parent,
          *title,
          *label,
          *text,
          ok,
          QFlags<Qt::WindowType>::fromInt(flags),
          QFlags<Qt::InputMethodHint>::fromInt(inputMethodHints)));
}

//  QString QInputDialog::getItem(QWidget *parent, const QString &title,
//      const QString &label, const QStringList &items, int current, bool
//      editable, bool *ok, Qt::WindowFlags flags, Qt::InputMethodHints
//      inputMethodHints)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDialog7getItemEP7QWidgetRK7QStringS4_RK5QListIS2_EibPb6QFlagsIN2Qt10WindowTypeEESA_INSB_15InputMethodHintEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    const QList<QString> *items,
    int current,
    bool editable,
    bool *ok,
    int flags,
    int inputMethodHints) {
  return new QString(
      QInputDialog::getItem(
          parent,
          *title,
          *label,
          *items,
          current,
          editable,
          ok,
          QFlags<Qt::WindowType>::fromInt(flags),
          QFlags<Qt::InputMethodHint>::fromInt(inputMethodHints)));
}

//  int QInputDialog::getInt(QWidget *parent, const QString &title, const
//      QString &label, int value, int minValue, int maxValue, int step, bool
//      *ok, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QInputDialog6getIntEP7QWidgetRK7QStringS4_iiiiPb6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    const QString *title,
    const QString *label,
    int value,
    int minValue,
    int maxValue,
    int step,
    bool *ok,
    int flags) {
  return QInputDialog::getInt(
      parent,
      *title,
      *label,
      value,
      minValue,
      maxValue,
      step,
      ok,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  double QInputDialog::getDouble(QWidget *parent, const QString &title,
//      const QString &label, double value, double minValue, double maxValue,
//      int decimals, bool *ok, Qt::WindowFlags flags, double step)
extern "C" Q_DECL_EXPORT
double ritual_ZN12QInputDialog9getDoubleEP7QWidgetRK7QStringS4_dddiPb6QFlagsIN2Qt10WindowTypeEEd(
    QWidget *parent,
    const QString *title,
    const QString *label,
    double value,
    double minValue,
    double maxValue,
    int decimals,
    bool *ok,
    int flags,
    double step) {
  return QInputDialog::getDouble(
      parent,
      *title,
      *label,
      value,
      minValue,
      maxValue,
      decimals,
      ok,
      QFlags<Qt::WindowType>::fromInt(flags),
      step);
}

//  void QInputDialog::setDoubleStep(double step)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog13setDoubleStepEd(
    QInputDialog *self,
    double step) {
  self->setDoubleStep(step);
}

//  double QInputDialog::doubleStep() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK12QInputDialog10doubleStepEv(const QInputDialog *self) {
  return self->doubleStep();
}

//  void QInputDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDialog4doneEi(QInputDialog *self, int result) {
  self->done(result);
}

//  a Python function taken by a CuteQInputDialog, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInputDialog(
    QInputDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInputDialog *>(self)->take(key, call);
}

//  QSize QInputDialog::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QInputDialog15minimumSizeHintEv(
    const QInputDialog *self) {
  return new QSize(self->QInputDialog::minimumSizeHint());
}

//  QSize QInputDialog::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QInputDialog8sizeHintEv(const QInputDialog *self) {
  return new QSize(self->QInputDialog::sizeHint());
}

//  void QInputDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QInputDialog10setVisibleEb(
    QInputDialog *self,
    bool visible) {
  self->QInputDialog::setVisible(visible);
}

//  void QInputDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QInputDialog4doneEi(QInputDialog *self, int result) {
  self->QInputDialog::done(result);
}

#endif  // QT_CONFIG(inputdialog)
#endif  // QT_CONFIG(inputdialog)
