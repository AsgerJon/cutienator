//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfontdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(fontdialog)
#if QT_CONFIG(fontdialog)
#include <QtWidgets/qfontdialog.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QFontDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFontDialog : QFontDialog {
  using QFontDialog::changeEvent;
  using QFontDialog::done;
  using QFontDialog::eventFilter;
};

//  A QFontDialog that Python can take functions over in. Every QFontDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(fontdialog)
typedef void (*CuteQFontDialogCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(fontdialog)
#if QT_CONFIG(fontdialog)
typedef void (*CuteQFontDialogCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(fontdialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
typedef void (*CuteQFontDialogCall2)(const void *, int, int *);
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(fontdialog)
typedef bool (*CuteQFontDialogCall3)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(fontdialog)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQFontDialogCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQFontDialogCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQFontDialogCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall8)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall9)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall11)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall12)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall13)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef int (*CuteQFontDialogCall15)(const void *, int *);
typedef int (*CuteQFontDialogCall16)(const void *, int, int *);
typedef bool (*CuteQFontDialogCall17)(const void *, int *);
typedef void * (*CuteQFontDialogCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFontDialogCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFontDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFontDialogCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFontDialogCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQFontDialogCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQFontDialogCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQFontDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFontDialogCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFontDialogCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQFontDialogCall29)(const void *, QEvent *, int *);
typedef void (*CuteQFontDialogCall30)(const void *, QPaintEvent *, int *);
typedef void (*CuteQFontDialogCall31)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQFontDialogCall32)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQFontDialogCall33)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontDialogCall34)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontDialogCall35)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontDialogCall36)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontDialogCall37)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQFontDialogCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQFontDialogCall39)(const void *, int, int *);
typedef void (*CuteQFontDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQFontDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQFontDialogCall42)(const void *, int *);
typedef void (*CuteQFontDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQFontDialogCall44)(const void *, int, int *);
typedef bool (*CuteQFontDialogCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontDialogCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontDialogCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontDialogCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontDialogCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontDialogCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFontDialog : public QFontDialog {
public:
  using QFontDialog::QFontDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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

#if QT_CONFIG(fontdialog)
  //  void QFontDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontDialogCall0 call = reinterpret_cast<CuteQFontDialogCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QFontDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(fontdialog)

#if QT_CONFIG(fontdialog)
  //  void QFontDialog::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontDialogCall1 call = reinterpret_cast<CuteQFontDialogCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QFontDialog::changeEvent(event);
  }
#endif  // QT_CONFIG(fontdialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
  //  void QFontDialog::done(int result)
  void done(int result) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontDialogCall2 call = reinterpret_cast<CuteQFontDialogCall2>(taken[2]);
      call(this, result, &handled);
      if (handled) return;
    }
    QFontDialog::done(result);
  }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(fontdialog)
  //  bool QFontDialog::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontDialogCall3 call = reinterpret_cast<CuteQFontDialogCall3>(taken[3]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QFontDialog::eventFilter(object, event);
  }
#endif  // QT_CONFIG(fontdialog)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontDialogCall4 call = reinterpret_cast<CuteQFontDialogCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontDialogCall5 call = reinterpret_cast<CuteQFontDialogCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontDialogCall6 call = reinterpret_cast<CuteQFontDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontDialogCall7 call = reinterpret_cast<CuteQFontDialogCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::accept()
  void accept() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontDialogCall8 call = reinterpret_cast<CuteQFontDialogCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontDialogCall9 call = reinterpret_cast<CuteQFontDialogCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontDialogCall10 call = reinterpret_cast<CuteQFontDialogCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontDialogCall11 call = reinterpret_cast<CuteQFontDialogCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontDialogCall12 call = reinterpret_cast<CuteQFontDialogCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontDialogCall13 call = reinterpret_cast<CuteQFontDialogCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQFontDialogCall14 call = reinterpret_cast<CuteQFontDialogCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFontDialogCall15 call = reinterpret_cast<CuteQFontDialogCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontDialogCall16 call = reinterpret_cast<CuteQFontDialogCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQFontDialogCall17 call = reinterpret_cast<CuteQFontDialogCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQFontDialogCall18 call = reinterpret_cast<CuteQFontDialogCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontDialogCall19 call = reinterpret_cast<CuteQFontDialogCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontDialogCall20 call = reinterpret_cast<CuteQFontDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontDialogCall21 call = reinterpret_cast<CuteQFontDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontDialogCall22 call = reinterpret_cast<CuteQFontDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontDialogCall23 call = reinterpret_cast<CuteQFontDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontDialogCall24 call = reinterpret_cast<CuteQFontDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontDialogCall25 call = reinterpret_cast<CuteQFontDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFontDialogCall26 call = reinterpret_cast<CuteQFontDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontDialogCall27 call = reinterpret_cast<CuteQFontDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontDialogCall28 call = reinterpret_cast<CuteQFontDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontDialogCall29 call = reinterpret_cast<CuteQFontDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontDialogCall30 call = reinterpret_cast<CuteQFontDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFontDialogCall31 call = reinterpret_cast<CuteQFontDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontDialogCall32 call = reinterpret_cast<CuteQFontDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontDialogCall33 call = reinterpret_cast<CuteQFontDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontDialogCall34 call = reinterpret_cast<CuteQFontDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontDialogCall35 call = reinterpret_cast<CuteQFontDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQFontDialogCall36 call = reinterpret_cast<CuteQFontDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQFontDialogCall37 call = reinterpret_cast<CuteQFontDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQFontDialogCall38 call = reinterpret_cast<CuteQFontDialogCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontDialogCall39 call = reinterpret_cast<CuteQFontDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQFontDialogCall40 call = reinterpret_cast<CuteQFontDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontDialogCall41 call = reinterpret_cast<CuteQFontDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQFontDialogCall42 call = reinterpret_cast<CuteQFontDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQFontDialogCall43 call = reinterpret_cast<CuteQFontDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontDialogCall44 call = reinterpret_cast<CuteQFontDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQFontDialogCall45 call = reinterpret_cast<CuteQFontDialogCall45>(taken[45]);
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
      CuteQFontDialogCall46 call = reinterpret_cast<CuteQFontDialogCall46>(taken[46]);
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
      CuteQFontDialogCall47 call = reinterpret_cast<CuteQFontDialogCall47>(taken[47]);
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
      CuteQFontDialogCall48 call = reinterpret_cast<CuteQFontDialogCall48>(taken[48]);
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
      CuteQFontDialogCall49 call = reinterpret_cast<CuteQFontDialogCall49>(taken[49]);
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
      CuteQFontDialogCall50 call = reinterpret_cast<CuteQFontDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFontDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFontDialog10metaObjectEv(
    const QFontDialog *self) {
  return self->metaObject();
}

//  void *QFontDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QFontDialog11qt_metacastEPKc(
    QFontDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QFontDialog::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QFontDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QFontDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QFontDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFontDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFontDialog::tr(s, c, n));
}

//  QFontDialogPrivate *QFontDialog::d_func()
extern "C" Q_DECL_EXPORT
QFontDialogPrivate *ritual_ZN11QFontDialog6d_funcEv(QFontDialog *self) {
  return self->d_func();
}

//  const QFontDialogPrivate *QFontDialog::d_func() const
extern "C" Q_DECL_EXPORT
const QFontDialogPrivate *ritual_ZNK11QFontDialog6d_funcEv(
    const QFontDialog *self) {
  return self->d_func();
}

//  QFontDialog::QFontDialog(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFontDialog *ritual_ZN11QFontDialogC1EP7QWidget(QWidget *parent) {
  return new CuteQFontDialog(parent);
}

//  QFontDialog::QFontDialog(const QFont &initial, QWidget *parent)
extern "C" Q_DECL_EXPORT
QFontDialog *ritual_ZN11QFontDialogC1ERK5QFontP7QWidget(
    const QFont *initial,
    QWidget *parent) {
  return new CuteQFontDialog(*initial, parent);
}

//  QFontDialog::~QFontDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialogD1Ev(QFontDialog *self) {
  delete self;
}

//  void QFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog14setCurrentFontERK5QFont(
    QFontDialog *self,
    const QFont *font) {
  self->setCurrentFont(*font);
}

//  QFont QFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QFontDialog11currentFontEv(const QFontDialog *self) {
  return new QFont(self->currentFont());
}

//  QFont QFontDialog::selectedFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QFontDialog12selectedFontEv(const QFontDialog *self) {
  return new QFont(self->selectedFont());
}

//  void QFontDialog::setOption(FontDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog9setOptionENS_16FontDialogOptionEb(
    QFontDialog *self,
    QFontDialog::FontDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFontDialog::testOption(FontDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontDialog10testOptionENS_16FontDialogOptionE(
    const QFontDialog *self,
    QFontDialog::FontDialogOption option) {
  return self->testOption(option);
}

//  void QFontDialog::setOptions(FontDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog10setOptionsE6QFlagsINS_16FontDialogOptionEE(
    QFontDialog *self,
    int options) {
  self->setOptions(QFlags<QFontDialog::FontDialogOption>::fromInt(options));
}

//  FontDialogOptions QFontDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFontDialog7optionsEv(const QFontDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QFontDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog4openEP7QObjectPKc(
    QFontDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QFontDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog10setVisibleEb(QFontDialog *self, bool visible) {
  self->setVisible(visible);
}

//  QFont QFontDialog::getFont(bool *ok, QWidget *parent)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN11QFontDialog7getFontEPbP7QWidget(
    bool *ok,
    QWidget *parent) {
  return new QFont(QFontDialog::getFont(ok, parent));
}

//  QFont QFontDialog::getFont(bool *ok, const QFont &initial, QWidget
//      *parent, const QString &title, FontDialogOptions options)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN11QFontDialog7getFontEPbRK5QFontP7QWidgetRK7QString6QFlagsINS_16FontDialogOptionEE(
    bool *ok,
    const QFont *initial,
    QWidget *parent,
    const QString *title,
    int options) {
  return new QFont(
      QFontDialog::getFont(
          ok,
          *initial,
          parent,
          *title,
          QFlags<QFontDialog::FontDialogOption>::fromInt(options)));
}

//  void QFontDialog::currentFontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog18currentFontChangedERK5QFont(
    QFontDialog *self,
    const QFont *font) {
  self->currentFontChanged(*font);
}

//  void QFontDialog::fontSelected(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog12fontSelectedERK5QFont(
    QFontDialog *self,
    const QFont *font) {
  self->fontSelected(*font);
}

//  void QFontDialog::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog11changeEventEP6QEvent(
    QFontDialog *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QFontDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontDialog4doneEi(QFontDialog *self, int result) {
  self->done(result);
}

//  bool QFontDialog::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFontDialog11eventFilterEP7QObjectP6QEvent(
    QFontDialog *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  a Python function taken by a CuteQFontDialog, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontDialog(
    QFontDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontDialog *>(self)->take(key, call);
}

//  void QFontDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontDialog10setVisibleEb(
    QFontDialog *self,
    bool visible) {
  self->QFontDialog::setVisible(visible);
}

//  void QFontDialog::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontDialog11changeEventEP6QEvent(
    QFontDialog *self,
    QEvent *event) {
  static_cast<OwnQFontDialog *>(self)->OwnQFontDialog::changeEvent(event);
}

//  void QFontDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontDialog4doneEi(QFontDialog *self, int result) {
  static_cast<OwnQFontDialog *>(self)->OwnQFontDialog::done(result);
}

//  bool QFontDialog::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFontDialog11eventFilterEP7QObjectP6QEvent(
    QFontDialog *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQFontDialog *>(self)->OwnQFontDialog::eventFilter(
      object,
      event);
}

#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(fontdialog)
