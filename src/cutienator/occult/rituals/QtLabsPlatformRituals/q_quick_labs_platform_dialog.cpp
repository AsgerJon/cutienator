//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformdialog_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 268, as _ZN24QQuickLabsPlatformDialog6acceptEv
inline void QQuickLabsPlatformDialog::accept()
{
    done(Accepted);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 280, as _ZN24QQuickLabsPlatformDialog6rejectEv
inline void QQuickLabsPlatformDialog::reject()
{
    done(Rejected);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 292, as _ZN24QQuickLabsPlatformDialog4doneEi
inline void QQuickLabsPlatformDialog::done(int result)
{
    close();
    setResult(result);

    if (result == Accepted)
        emit accepted();
    else if (result == Rejected)
        emit rejected();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 342, as _ZNK24QQuickLabsPlatformDialog15useNativeDialogEv
inline bool QQuickLabsPlatformDialog::useNativeDialog() const
{
    return !QCoreApplication::testAttribute(Qt::AA_DontUseNativeDialogs)
            && QGuiApplicationPrivate::platformTheme()->usePlatformNativeDialog(m_type);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 348, as _ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDialogHelper
inline void QQuickLabsPlatformDialog::onCreate(QPlatformDialogHelper *dialog)
{
    Q_UNUSED(dialog);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 353, as _ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialogHelper
inline void QQuickLabsPlatformDialog::onShow(QPlatformDialogHelper *dialog)
{
    Q_UNUSED(dialog);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 358, as _ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialogHelper
inline void QQuickLabsPlatformDialog::onHide(QPlatformDialogHelper *dialog)
{
    Q_UNUSED(dialog);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 250, as _ZN24QQuickLabsPlatformDialog5closeEv
inline void QQuickLabsPlatformDialog::close()
{
    if (!m_handle || !m_visible)
        return;

    onHide(m_handle);
    m_handle->hide();
    m_visible = false;
    emit visibleChanged();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 72, as _ZN24QQuickLabsPlatformDialogD1Ev
inline QQuickLabsPlatformDialog::~QQuickLabsPlatformDialog()
{
    destroy();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 77, as _ZNK24QQuickLabsPlatformDialog6handleEv
inline QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 103, as _ZNK24QQuickLabsPlatformDialog12parentWindowEv
inline QWindow *QQuickLabsPlatformDialog::parentWindow() const
{
    return m_parentWindow;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 122, as _ZNK24QQuickLabsPlatformDialog5titleEv
inline QString QQuickLabsPlatformDialog::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 141, as _ZNK24QQuickLabsPlatformDialog5flagsEv
inline Qt::WindowFlags QQuickLabsPlatformDialog::flags() const
{
    return m_flags;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 165, as _ZNK24QQuickLabsPlatformDialog8modalityEv
inline Qt::WindowModality QQuickLabsPlatformDialog::modality() const
{
    return m_modality;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 186, as _ZNK24QQuickLabsPlatformDialog9isVisibleEv
inline bool QQuickLabsPlatformDialog::isVisible() const
{
    return m_handle && m_visible;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 211, as _ZNK24QQuickLabsPlatformDialog6resultEv
inline int QQuickLabsPlatformDialog::result() const
{
    return m_result;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 303, as _ZN24QQuickLabsPlatformDialog10classBeginEv
inline void QQuickLabsPlatformDialog::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 307, as _ZN24QQuickLabsPlatformDialog17componentCompleteEv
inline void QQuickLabsPlatformDialog::componentComplete()
{
    m_complete = true;
    if (!m_parentWindow)
        setParentWindow(findParentWindow());
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 336, as _ZN24QQuickLabsPlatformDialog7destroyEv
inline void QQuickLabsPlatformDialog::destroy()
{
    delete m_handle;
    m_handle = nullptr;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 363, as _ZNK24QQuickLabsPlatformDialog16findParentWindowEv
inline QWindow *QQuickLabsPlatformDialog::findParentWindow() const
{
    QObject *obj = parent();
    while (obj) {
        QWindow *window = qobject_cast<QWindow *>(obj);
        if (window)
            return window;
        QQuickItem *item = qobject_cast<QQuickItem *>(obj);
        if (item && item->window())
            return item->window();
        obj = obj->parent();
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformDialog : QQuickLabsPlatformDialog {
  using QQuickLabsPlatformDialog::classBegin;
  using QQuickLabsPlatformDialog::useNativeDialog;
  using QQuickLabsPlatformDialog::onCreate;
  using QQuickLabsPlatformDialog::onShow;
  using QQuickLabsPlatformDialog::onHide;
};

//  A QQuickLabsPlatformDialog that Python can take functions over in. Every QQuickLabsPlatformDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLabsPlatformDialogCall0)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall1)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall2)(const void *, int, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall3)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall4)(const void *, int *);
typedef bool (*CuteQQuickLabsPlatformDialogCall5)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall6)(const void *, QPlatformDialogHelper *, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall7)(const void *, QPlatformDialogHelper *, int *);
typedef void (*CuteQQuickLabsPlatformDialogCall8)(const void *, QPlatformDialogHelper *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformDialogCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformDialogCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformDialogCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformDialogCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformDialogCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformDialogCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformDialogCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformDialog : public QQuickLabsPlatformDialog {
public:
  using QQuickLabsPlatformDialog::QQuickLabsPlatformDialog;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickLabsPlatformDialog6acceptEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickLabsPlatformDialog6rejectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickLabsPlatformDialog4doneEi")) {
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
    if (!std::strcmp(key, "_ZNK24QQuickLabsPlatformDialog15useNativeDialogEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDialogHelper")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialogHelper")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialogHelper")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickLabsPlatformDialog::accept()
  void accept() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall0 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::accept();
  }

  //  void QQuickLabsPlatformDialog::reject()
  void reject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall1 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::reject();
  }

  //  void QQuickLabsPlatformDialog::done(int result)
  void done(int result) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall2 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall2>(taken[2]);
      call(this, result, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::done(result);
  }

  //  void QQuickLabsPlatformDialog::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall3 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::classBegin();
  }

  //  void QQuickLabsPlatformDialog::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall4 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::componentComplete();
  }

  //  bool QQuickLabsPlatformDialog::useNativeDialog() const
  bool useNativeDialog() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall5 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickLabsPlatformDialog::useNativeDialog();
  }

  //  void QQuickLabsPlatformDialog::onCreate(QPlatformDialogHelper
  //      *dialog)
  void onCreate(QPlatformDialogHelper *dialog) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall6 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall6>(taken[6]);
      call(this, dialog, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::onCreate(dialog);
  }

  //  void QQuickLabsPlatformDialog::onShow(QPlatformDialogHelper *dialog)
  void onShow(QPlatformDialogHelper *dialog) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall7 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall7>(taken[7]);
      call(this, dialog, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::onShow(dialog);
  }

  //  void QQuickLabsPlatformDialog::onHide(QPlatformDialogHelper *dialog)
  void onHide(QPlatformDialogHelper *dialog) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall8 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall8>(taken[8]);
      call(this, dialog, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformDialog::onHide(dialog);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall9 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall10 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall11 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall12 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall13 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall14 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLabsPlatformDialogCall15 call = reinterpret_cast<CuteQQuickLabsPlatformDialogCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickLabsPlatformDialog10metaObjectEv(
    const QQuickLabsPlatformDialog *self) {
  return self->metaObject();
}

//  void QQuickLabsPlatformDialog::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog24qt_qmlMarker_uncreatableEv(
    QQuickLabsPlatformDialog *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickLabsPlatformDialog::~QQuickLabsPlatformDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialogD1Ev(
    QQuickLabsPlatformDialog *self) {
  delete self;
}

//  QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper *ritual_ZNK24QQuickLabsPlatformDialog6handleEv(
    const QQuickLabsPlatformDialog *self) {
  return self->handle();
}

//  QWindow *QQuickLabsPlatformDialog::parentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK24QQuickLabsPlatformDialog12parentWindowEv(
    const QQuickLabsPlatformDialog *self) {
  return self->parentWindow();
}

//  QString QQuickLabsPlatformDialog::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickLabsPlatformDialog5titleEv(
    const QQuickLabsPlatformDialog *self) {
  return new QString(self->title());
}

//  Qt::WindowFlags QQuickLabsPlatformDialog::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickLabsPlatformDialog5flagsEv(
    const QQuickLabsPlatformDialog *self) {
  return static_cast<int>(self->flags().toInt());
}

//  Qt::WindowModality QQuickLabsPlatformDialog::modality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK24QQuickLabsPlatformDialog8modalityEv(
    const QQuickLabsPlatformDialog *self) {
  return self->modality();
}

//  bool QQuickLabsPlatformDialog::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickLabsPlatformDialog9isVisibleEv(
    const QQuickLabsPlatformDialog *self) {
  return self->isVisible();
}

//  int QQuickLabsPlatformDialog::result() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickLabsPlatformDialog6resultEv(
    const QQuickLabsPlatformDialog *self) {
  return self->result();
}

//  void QQuickLabsPlatformDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog6acceptEv(
    QQuickLabsPlatformDialog *self) {
  self->accept();
}

//  void QQuickLabsPlatformDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog6rejectEv(
    QQuickLabsPlatformDialog *self) {
  self->reject();
}

//  void QQuickLabsPlatformDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog4doneEi(
    QQuickLabsPlatformDialog *self,
    int result) {
  self->done(result);
}

//  void QQuickLabsPlatformDialog::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog10classBeginEv(
    QQuickLabsPlatformDialog *self) {
  self->classBegin();
}

//  void QQuickLabsPlatformDialog::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog17componentCompleteEv(
    QQuickLabsPlatformDialog *self) {
  self->componentComplete();
}

//  void QQuickLabsPlatformDialog::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog7destroyEv(
    QQuickLabsPlatformDialog *self) {
  self->destroy();
}

//  bool QQuickLabsPlatformDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickLabsPlatformDialog15useNativeDialogEv(
    const QQuickLabsPlatformDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickLabsPlatformDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickLabsPlatformDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialogHelper(
    QQuickLabsPlatformDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onHide(dialog);
}

//  QWindow *QQuickLabsPlatformDialog::findParentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK24QQuickLabsPlatformDialog16findParentWindowEv(
    const QQuickLabsPlatformDialog *self) {
  return self->findParentWindow();
}

//  QQuickLabsPlatformDialog as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickLabsPlatformDialog_QQmlParserStatus(
    QQuickLabsPlatformDialog *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickLabsPlatformDialog, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformDialog(
    QQuickLabsPlatformDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformDialog *>(self)->take(key, call);
}

//  void QQuickLabsPlatformDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickLabsPlatformDialog6acceptEv(
    QQuickLabsPlatformDialog *self) {
  self->QQuickLabsPlatformDialog::accept();
}

//  void QQuickLabsPlatformDialog::reject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickLabsPlatformDialog6rejectEv(
    QQuickLabsPlatformDialog *self) {
  self->QQuickLabsPlatformDialog::reject();
}

//  void QQuickLabsPlatformDialog::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickLabsPlatformDialog10classBeginEv(
    QQuickLabsPlatformDialog *self) {
  static_cast<OwnQQuickLabsPlatformDialog *>(self)->OwnQQuickLabsPlatformDialog::classBegin();
}

//  bool QQuickLabsPlatformDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQuickLabsPlatformDialog15useNativeDialogEv(
    const QQuickLabsPlatformDialog *self) {
  return static_cast<const OwnQQuickLabsPlatformDialog *>(self)->OwnQQuickLabsPlatformDialog::useNativeDialog();
}

//  void QQuickLabsPlatformDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickLabsPlatformDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformDialog *>(self)->OwnQQuickLabsPlatformDialog::onCreate(
      dialog);
}

//  void QQuickLabsPlatformDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickLabsPlatformDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformDialog *>(self)->OwnQQuickLabsPlatformDialog::onShow(
      dialog);
}

//  void QQuickLabsPlatformDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickLabsPlatformDialog6onHideEP21QPlatformDialogHelper(
    QQuickLabsPlatformDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformDialog *>(self)->OwnQQuickLabsPlatformDialog::onHide(
      dialog);
}
