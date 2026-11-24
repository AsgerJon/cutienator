//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickabstractdialog_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qtquickdialogs2global_p.h>
#include <QtQuickDialogs2/QtQuickDialogs2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickabstractdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickAbstractDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAbstractDialog : QQuickAbstractDialog {
  using QQuickAbstractDialog::classBegin;
  using QQuickAbstractDialog::componentComplete;
  using QQuickAbstractDialog::useNativeDialog;
  using QQuickAbstractDialog::onCreate;
  using QQuickAbstractDialog::onShow;
  using QQuickAbstractDialog::onHide;
  using QQuickAbstractDialog::dialogCode;
};

//  A QQuickAbstractDialog that Python can take functions over in. Every QQuickAbstractDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAbstractDialogCall0)(const void *, int *);
typedef void (*CuteQQuickAbstractDialogCall1)(const void *, int *);
typedef void (*CuteQQuickAbstractDialogCall2)(const void *, int, int *);
typedef void (*CuteQQuickAbstractDialogCall3)(const void *, int *);
typedef void (*CuteQQuickAbstractDialogCall4)(const void *, int *);
typedef bool (*CuteQQuickAbstractDialogCall5)(const void *, int *);
typedef void (*CuteQQuickAbstractDialogCall6)(const void *, QPlatformDialogHelper *, int *);
typedef void (*CuteQQuickAbstractDialogCall7)(const void *, QPlatformDialogHelper *, int *);
typedef void (*CuteQQuickAbstractDialogCall8)(const void *, QPlatformDialogHelper *, int *);
typedef int (*CuteQQuickAbstractDialogCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractDialogCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractDialogCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractDialogCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractDialogCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractDialogCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractDialogCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractDialogCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAbstractDialog : public QQuickAbstractDialog {
public:
  using QQuickAbstractDialog::QQuickAbstractDialog;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickAbstractDialog6acceptEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractDialog6rejectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractDialog4doneEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickAbstractDialog15useNativeDialogEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractDialog8onCreateEP21QPlatformDialogHelper")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractDialog6onShowEP21QPlatformDialogHelper")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAbstractDialog6onHideEP21QPlatformDialogHelper")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickAbstractDialog10dialogCodeEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAbstractDialog::accept()
  void accept() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall0 call = reinterpret_cast<CuteQQuickAbstractDialogCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::accept();
  }

  //  void QQuickAbstractDialog::reject()
  void reject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall1 call = reinterpret_cast<CuteQQuickAbstractDialogCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::reject();
  }

  //  void QQuickAbstractDialog::done(int result)
  void done(int result) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall2 call = reinterpret_cast<CuteQQuickAbstractDialogCall2>(taken[2]);
      call(this, result, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::done(result);
  }

  //  void QQuickAbstractDialog::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall3 call = reinterpret_cast<CuteQQuickAbstractDialogCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::classBegin();
  }

  //  void QQuickAbstractDialog::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall4 call = reinterpret_cast<CuteQQuickAbstractDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::componentComplete();
  }

  //  bool QQuickAbstractDialog::useNativeDialog() const
  bool useNativeDialog() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall5 call = reinterpret_cast<CuteQQuickAbstractDialogCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAbstractDialog::useNativeDialog();
  }

  //  void QQuickAbstractDialog::onCreate(QPlatformDialogHelper *dialog)
  void onCreate(QPlatformDialogHelper *dialog) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall6 call = reinterpret_cast<CuteQQuickAbstractDialogCall6>(taken[6]);
      call(this, dialog, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::onCreate(dialog);
  }

  //  void QQuickAbstractDialog::onShow(QPlatformDialogHelper *dialog)
  void onShow(QPlatformDialogHelper *dialog) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall7 call = reinterpret_cast<CuteQQuickAbstractDialogCall7>(taken[7]);
      call(this, dialog, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::onShow(dialog);
  }

  //  void QQuickAbstractDialog::onHide(QPlatformDialogHelper *dialog)
  void onHide(QPlatformDialogHelper *dialog) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall8 call = reinterpret_cast<CuteQQuickAbstractDialogCall8>(taken[8]);
      call(this, dialog, &handled);
      if (handled) return;
    }
    QQuickAbstractDialog::onHide(dialog);
  }

  //  int QQuickAbstractDialog::dialogCode() const
  int dialogCode() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall9 call = reinterpret_cast<CuteQQuickAbstractDialogCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAbstractDialog::dialogCode();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall10 call = reinterpret_cast<CuteQQuickAbstractDialogCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall11 call = reinterpret_cast<CuteQQuickAbstractDialogCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall12 call = reinterpret_cast<CuteQQuickAbstractDialogCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall13 call = reinterpret_cast<CuteQQuickAbstractDialogCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall14 call = reinterpret_cast<CuteQQuickAbstractDialogCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall15 call = reinterpret_cast<CuteQQuickAbstractDialogCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAbstractDialogCall16 call = reinterpret_cast<CuteQQuickAbstractDialogCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAbstractDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickAbstractDialog10metaObjectEv(
    const QQuickAbstractDialog *self) {
  return self->metaObject();
}

//  QString QQuickAbstractDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickAbstractDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAbstractDialog::tr(s, c, n));
}

//  void QQuickAbstractDialog::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog22qt_qmlMarker_anonymousEv(
    QQuickAbstractDialog *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickAbstractDialog::QQuickAbstractDialog(QQuickDialogType type, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickAbstractDialog *ritual_ZN20QQuickAbstractDialogC1E16QQuickDialogTypeP7QObject(
    QQuickDialogType type,
    QObject *parent) {
  return new CuteQQuickAbstractDialog(type, parent);
}

//  QQuickAbstractDialog::~QQuickAbstractDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialogD1Ev(QQuickAbstractDialog *self) {
  delete self;
}

//  QPlatformDialogHelper *QQuickAbstractDialog::handle() const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper *ritual_ZNK20QQuickAbstractDialog6handleEv(
    const QQuickAbstractDialog *self) {
  return self->handle();
}

//  QWindow *QQuickAbstractDialog::parentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK20QQuickAbstractDialog12parentWindowEv(
    const QQuickAbstractDialog *self) {
  return self->parentWindow();
}

//  void QQuickAbstractDialog::setParentWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog15setParentWindowEP7QWindow(
    QQuickAbstractDialog *self,
    QWindow *window) {
  self->setParentWindow(window);
}

//  void QQuickAbstractDialog::resetParentWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog17resetParentWindowEv(
    QQuickAbstractDialog *self) {
  self->resetParentWindow();
}

//  QString QQuickAbstractDialog::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickAbstractDialog5titleEv(
    const QQuickAbstractDialog *self) {
  return new QString(self->title());
}

//  void QQuickAbstractDialog::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog8setTitleERK7QString(
    QQuickAbstractDialog *self,
    const QString *title) {
  self->setTitle(*title);
}

//  Qt::WindowFlags QQuickAbstractDialog::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAbstractDialog5flagsEv(
    const QQuickAbstractDialog *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QQuickAbstractDialog::setFlags(Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog8setFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QQuickAbstractDialog *self,
    int flags) {
  self->setFlags(QFlags<Qt::WindowType>::fromInt(flags));
}

//  Qt::WindowModality QQuickAbstractDialog::modality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK20QQuickAbstractDialog8modalityEv(
    const QQuickAbstractDialog *self) {
  return self->modality();
}

//  void QQuickAbstractDialog::setModality(Qt::WindowModality modality)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog11setModalityEN2Qt14WindowModalityE(
    QQuickAbstractDialog *self,
    Qt::WindowModality modality) {
  self->setModality(modality);
}

//  bool QQuickAbstractDialog::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractDialog9isVisibleEv(
    const QQuickAbstractDialog *self) {
  return self->isVisible();
}

//  void QQuickAbstractDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog10setVisibleEb(
    QQuickAbstractDialog *self,
    bool visible) {
  self->setVisible(visible);
}

//  int QQuickAbstractDialog::result() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAbstractDialog6resultEv(
    const QQuickAbstractDialog *self) {
  return self->result();
}

//  void QQuickAbstractDialog::setResult(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog9setResultEi(
    QQuickAbstractDialog *self,
    int result) {
  self->setResult(result);
}

//  QQuickPopup::PopupType QQuickAbstractDialog::popupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_ZNK20QQuickAbstractDialog9popupTypeEv(
    const QQuickAbstractDialog *self) {
  return self->popupType();
}

//  void QQuickAbstractDialog::setPopupType(QQuickPopup::PopupType popupType)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog12setPopupTypeEN11QQuickPopup9PopupTypeE(
    QQuickAbstractDialog *self,
    QQuickPopup::PopupType popupType) {
  self->setPopupType(popupType);
}

//  void QQuickAbstractDialog::resetPopupType()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog14resetPopupTypeEv(
    QQuickAbstractDialog *self) {
  self->resetPopupType();
}

//  void QQuickAbstractDialog::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog4openEv(QQuickAbstractDialog *self) {
  self->open();
}

//  void QQuickAbstractDialog::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog5closeEv(QQuickAbstractDialog *self) {
  self->close();
}

//  void QQuickAbstractDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog6acceptEv(QQuickAbstractDialog *self) {
  self->accept();
}

//  void QQuickAbstractDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog6rejectEv(QQuickAbstractDialog *self) {
  self->reject();
}

//  void QQuickAbstractDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog4doneEi(
    QQuickAbstractDialog *self,
    int result) {
  self->done(result);
}

//  void QQuickAbstractDialog::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog10classBeginEv(
    QQuickAbstractDialog *self) {
  self->classBegin();
}

//  void QQuickAbstractDialog::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog17componentCompleteEv(
    QQuickAbstractDialog *self) {
  self->componentComplete();
}

//  bool QQuickAbstractDialog::create(CreateOptions a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickAbstractDialog6createENS_13CreateOptionsE(
    QQuickAbstractDialog *self,
    QQuickAbstractDialog::CreateOptions a0) {
  return self->create(a0);
}

//  void QQuickAbstractDialog::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog7destroyEv(QQuickAbstractDialog *self) {
  self->destroy();
}

//  bool QQuickAbstractDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAbstractDialog15useNativeDialogEv(
    const QQuickAbstractDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickAbstractDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog8onCreateEP21QPlatformDialogHelper(
    QQuickAbstractDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickAbstractDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog6onShowEP21QPlatformDialogHelper(
    QQuickAbstractDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickAbstractDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog6onHideEP21QPlatformDialogHelper(
    QQuickAbstractDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onHide(dialog);
}

//  int QQuickAbstractDialog::dialogCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickAbstractDialog10dialogCodeEv(
    const QQuickAbstractDialog *self) {
  return self->dialogCode();
}

//  QQuickItem *QQuickAbstractDialog::findParentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickAbstractDialog14findParentItemEv(
    const QQuickAbstractDialog *self) {
  return self->findParentItem();
}

//  QWindow *QQuickAbstractDialog::windowForOpen() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK20QQuickAbstractDialog13windowForOpenEv(
    const QQuickAbstractDialog *self) {
  return self->windowForOpen();
}

//  void QQuickAbstractDialog::deferredOpen(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAbstractDialog12deferredOpenEP7QWindow(
    QQuickAbstractDialog *self,
    QWindow *window) {
  self->deferredOpen(window);
}

//  QQuickAbstractDialog as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickAbstractDialog_QQmlParserStatus(
    QQuickAbstractDialog *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickAbstractDialog, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractDialog(
    QQuickAbstractDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractDialog *>(self)->take(key, call);
}

//  void QQuickAbstractDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog6acceptEv(
    QQuickAbstractDialog *self) {
  self->QQuickAbstractDialog::accept();
}

//  void QQuickAbstractDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog6rejectEv(
    QQuickAbstractDialog *self) {
  self->QQuickAbstractDialog::reject();
}

//  void QQuickAbstractDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog4doneEi(
    QQuickAbstractDialog *self,
    int result) {
  self->QQuickAbstractDialog::done(result);
}

//  void QQuickAbstractDialog::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog10classBeginEv(
    QQuickAbstractDialog *self) {
  static_cast<OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::classBegin();
}

//  void QQuickAbstractDialog::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog17componentCompleteEv(
    QQuickAbstractDialog *self) {
  static_cast<OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::componentComplete();
}

//  bool QQuickAbstractDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QQuickAbstractDialog15useNativeDialogEv(
    const QQuickAbstractDialog *self) {
  return static_cast<const OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::useNativeDialog();
}

//  void QQuickAbstractDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog8onCreateEP21QPlatformDialogHelper(
    QQuickAbstractDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::onCreate(
      dialog);
}

//  void QQuickAbstractDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog6onShowEP21QPlatformDialogHelper(
    QQuickAbstractDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::onShow(
      dialog);
}

//  void QQuickAbstractDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickAbstractDialog6onHideEP21QPlatformDialogHelper(
    QQuickAbstractDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::onHide(
      dialog);
}

//  int QQuickAbstractDialog::dialogCode() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QQuickAbstractDialog10dialogCodeEv(
    const QQuickAbstractDialog *self) {
  return static_cast<const OwnQQuickAbstractDialog *>(self)->OwnQQuickAbstractDialog::dialogCode();
}
