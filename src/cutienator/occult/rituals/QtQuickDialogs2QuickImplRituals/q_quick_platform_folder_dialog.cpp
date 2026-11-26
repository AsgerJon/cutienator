//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfolderdi
//  alog_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfolderdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickPlatformFolderDialog that Python can take functions over in. Every QQuickPlatformFolderDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickPlatformFolderDialogCall0)(const void *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall1)(const void *, const QUrl *, int *);
typedef const QUrl * (*CuteQQuickPlatformFolderDialogCall2)(const void *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall3)(const void *, const QUrl *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall4)(const void *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall5)(const void *, const QString *, int *);
typedef QString * (*CuteQQuickPlatformFolderDialogCall6)(const void *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall7)(const void *, int *);
typedef bool (*CuteQQuickPlatformFolderDialogCall8)(const void *, int, int, QWindow *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall9)(const void *, int *);
typedef void (*CuteQQuickPlatformFolderDialogCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQQuickPlatformFolderDialogCall11)(const void *, int *);
typedef bool (*CuteQQuickPlatformFolderDialogCall12)(const void *, const QUrl *, int *);
typedef const QVariant * (*CuteQQuickPlatformFolderDialogCall13)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformFolderDialogCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformFolderDialogCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFolderDialogCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFolderDialogCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFolderDialogCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFolderDialogCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFolderDialogCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlatformFolderDialog : public QQuickPlatformFolderDialog {
public:
  using QQuickPlatformFolderDialog::QQuickPlatformFolderDialog;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QPlatformFileDialogHelper25defaultNameFilterDisablesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformFileDialogHelper12setDirectoryERK4QUrl")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformFileDialogHelper9directoryEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformFileDialogHelper10selectFileERK4QUrl")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformFileDialogHelper9setFilterEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformFileDialogHelper16selectNameFilterERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformFileDialogHelper18selectedNameFilterEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4execEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformDialogHelper4hideEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPlatformFileDialogHelper20selectMimeTypeFilterERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformFileDialogHelper22selectedMimeTypeFilterEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformFileDialogHelper14isSupportedUrlERK4QUrl")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQuickPlatformFolderDialog::defaultNameFilterDisables() const
  bool defaultNameFilterDisables() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall0 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPlatformFolderDialog::defaultNameFilterDisables();
  }

  //  void QQuickPlatformFolderDialog::setDirectory(const QUrl &directory)
  void setDirectory(const QUrl &directory) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall1 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall1>(taken[1]);
      call(this, &directory, &handled);
      if (handled) return;
    }
    QQuickPlatformFolderDialog::setDirectory(directory);
  }

  //  QUrl QQuickPlatformFolderDialog::directory() const
  QUrl directory() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall2 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall2>(taken[2]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPlatformFolderDialog::directory();
  }

  //  void QQuickPlatformFolderDialog::selectFile(const QUrl &file)
  void selectFile(const QUrl &file) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall3 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall3>(taken[3]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QQuickPlatformFolderDialog::selectFile(file);
  }

  //  void QQuickPlatformFolderDialog::setFilter()
  void setFilter() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall4 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFolderDialog::setFilter();
  }

  //  void QQuickPlatformFolderDialog::selectNameFilter(const QString
  //      &filter)
  void selectNameFilter(const QString &filter) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall5 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall5>(taken[5]);
      call(this, &filter, &handled);
      if (handled) return;
    }
    QQuickPlatformFolderDialog::selectNameFilter(filter);
  }

  //  QString QQuickPlatformFolderDialog::selectedNameFilter() const
  QString selectedNameFilter() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall6 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickPlatformFolderDialog::selectedNameFilter();
  }

  //  void QQuickPlatformFolderDialog::exec()
  void exec() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall7 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFolderDialog::exec();
  }

  //  bool QQuickPlatformFolderDialog::show(Qt::WindowFlags flags,
  //      Qt::WindowModality modality, QWindow *parent)
  bool show(
      Qt::WindowFlags flags,
      Qt::WindowModality modality,
      QWindow *parent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall8 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall8>(taken[8]);
      bool given = call(this, static_cast<int>(flags.toInt()), static_cast<int>(modality), parent, &handled);
      if (handled) return given;
    }
    return QQuickPlatformFolderDialog::show(flags, modality, parent);
  }

  //  void QQuickPlatformFolderDialog::hide()
  void hide() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall9 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFolderDialog::hide();
  }

  //  void QPlatformFileDialogHelper::selectMimeTypeFilter(const QString
  //      &filter)
  void selectMimeTypeFilter(const QString &filter) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall10 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall10>(taken[10]);
      call(this, &filter, &handled);
      if (handled) return;
    }
    QPlatformFileDialogHelper::selectMimeTypeFilter(filter);
  }

  //  QString QPlatformFileDialogHelper::selectedMimeTypeFilter() const
  QString selectedMimeTypeFilter() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall11 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall11>(taken[11]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformFileDialogHelper::selectedMimeTypeFilter();
  }

  //  bool QPlatformFileDialogHelper::isSupportedUrl(const QUrl &url) const
  bool isSupportedUrl(const QUrl &url) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall12 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall12>(taken[12]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QPlatformFileDialogHelper::isSupportedUrl(url);
  }

  //  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformDialogHelper::StyleHint hint) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall13 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall13>(taken[13]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QPlatformDialogHelper::styleHint(hint);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall14 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall15 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall16 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall17 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall18 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall19 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPlatformFolderDialogCall20 call = reinterpret_cast<CuteQQuickPlatformFolderDialogCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlatformFolderDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickPlatformFolderDialog10metaObjectEv(
    const QQuickPlatformFolderDialog *self) {
  return self->metaObject();
}

//  void *QQuickPlatformFolderDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuickPlatformFolderDialog11qt_metacastEPKc(
    QQuickPlatformFolderDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPlatformFolderDialog::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQuickPlatformFolderDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPlatformFolderDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPlatformFolderDialog::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickPlatformFolderDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlatformFolderDialog::tr(s, c, n));
}

//  QQuickPlatformFolderDialog::QQuickPlatformFolderDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlatformFolderDialog *ritual_ZN26QQuickPlatformFolderDialogC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlatformFolderDialog(parent);
}

//  QQuickPlatformFolderDialog::~QQuickPlatformFolderDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialogD1Ev(
    QQuickPlatformFolderDialog *self) {
  delete self;
}

//  bool QQuickPlatformFolderDialog::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickPlatformFolderDialog7isValidEv(
    const QQuickPlatformFolderDialog *self) {
  return self->isValid();
}

//  bool QQuickPlatformFolderDialog::defaultNameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickPlatformFolderDialog25defaultNameFilterDisablesEv(
    const QQuickPlatformFolderDialog *self) {
  return self->defaultNameFilterDisables();
}

//  void QQuickPlatformFolderDialog::setDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialog12setDirectoryERK4QUrl(
    QQuickPlatformFolderDialog *self,
    const QUrl *directory) {
  self->setDirectory(*directory);
}

//  QUrl QQuickPlatformFolderDialog::directory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK26QQuickPlatformFolderDialog9directoryEv(
    const QQuickPlatformFolderDialog *self) {
  return new QUrl(self->directory());
}

//  void QQuickPlatformFolderDialog::selectFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialog10selectFileERK4QUrl(
    QQuickPlatformFolderDialog *self,
    const QUrl *file) {
  self->selectFile(*file);
}

//  QList<QUrl> QQuickPlatformFolderDialog::selectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK26QQuickPlatformFolderDialog13selectedFilesEv(
    const QQuickPlatformFolderDialog *self) {
  return new QList<QUrl>(self->selectedFiles());
}

//  void QQuickPlatformFolderDialog::setFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialog9setFilterEv(
    QQuickPlatformFolderDialog *self) {
  self->setFilter();
}

//  void QQuickPlatformFolderDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialog16selectNameFilterERK7QString(
    QQuickPlatformFolderDialog *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QString QQuickPlatformFolderDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QQuickPlatformFolderDialog18selectedNameFilterEv(
    const QQuickPlatformFolderDialog *self) {
  return new QString(self->selectedNameFilter());
}

//  void QQuickPlatformFolderDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialog4execEv(
    QQuickPlatformFolderDialog *self) {
  self->exec();
}

//  bool QQuickPlatformFolderDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickPlatformFolderDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformFolderDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformFolderDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPlatformFolderDialog4hideEv(
    QQuickPlatformFolderDialog *self) {
  self->hide();
}

//  QQuickFolderDialogImpl *QQuickPlatformFolderDialog::dialog() const
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImpl *ritual_ZNK26QQuickPlatformFolderDialog6dialogEv(
    const QQuickPlatformFolderDialog *self) {
  return self->dialog();
}

//  a Python function taken by a CuteQQuickPlatformFolderDialog, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlatformFolderDialog(
    QQuickPlatformFolderDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlatformFolderDialog *>(self)->take(key, call);
}

//  bool QQuickPlatformFolderDialog::defaultNameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QQuickPlatformFolderDialog25defaultNameFilterDisablesEv(
    const QQuickPlatformFolderDialog *self) {
  return self->QQuickPlatformFolderDialog::defaultNameFilterDisables();
}

//  void QQuickPlatformFolderDialog::setDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPlatformFolderDialog12setDirectoryERK4QUrl(
    QQuickPlatformFolderDialog *self,
    const QUrl *directory) {
  self->QQuickPlatformFolderDialog::setDirectory(*directory);
}

//  QUrl QQuickPlatformFolderDialog::directory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK26QQuickPlatformFolderDialog9directoryEv(
    const QQuickPlatformFolderDialog *self) {
  return new QUrl(self->QQuickPlatformFolderDialog::directory());
}

//  void QQuickPlatformFolderDialog::selectFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPlatformFolderDialog10selectFileERK4QUrl(
    QQuickPlatformFolderDialog *self,
    const QUrl *file) {
  self->QQuickPlatformFolderDialog::selectFile(*file);
}

//  void QQuickPlatformFolderDialog::setFilter()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPlatformFolderDialog9setFilterEv(
    QQuickPlatformFolderDialog *self) {
  self->QQuickPlatformFolderDialog::setFilter();
}

//  void QQuickPlatformFolderDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPlatformFolderDialog16selectNameFilterERK7QString(
    QQuickPlatformFolderDialog *self,
    const QString *filter) {
  self->QQuickPlatformFolderDialog::selectNameFilter(*filter);
}

//  QString QQuickPlatformFolderDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QQuickPlatformFolderDialog18selectedNameFilterEv(
    const QQuickPlatformFolderDialog *self) {
  return new QString(self->QQuickPlatformFolderDialog::selectedNameFilter());
}

//  void QQuickPlatformFolderDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPlatformFolderDialog4execEv(
    QQuickPlatformFolderDialog *self) {
  self->QQuickPlatformFolderDialog::exec();
}

//  bool QQuickPlatformFolderDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QQuickPlatformFolderDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformFolderDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->QQuickPlatformFolderDialog::show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformFolderDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPlatformFolderDialog4hideEv(
    QQuickPlatformFolderDialog *self) {
  self->QQuickPlatformFolderDialog::hide();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
