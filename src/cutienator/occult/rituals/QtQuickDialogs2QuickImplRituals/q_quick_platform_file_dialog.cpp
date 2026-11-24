//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfiledial
//  og_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickPlatformFileDialog that Python can take functions over in. Every QQuickPlatformFileDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickPlatformFileDialogCall0)(const void *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall1)(const void *, const QUrl *, int *);
typedef const QUrl * (*CuteQQuickPlatformFileDialogCall2)(const void *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall3)(const void *, const QUrl *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall4)(const void *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall5)(const void *, const QString *, int *);
typedef QString * (*CuteQQuickPlatformFileDialogCall6)(const void *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall7)(const void *, int *);
typedef bool (*CuteQQuickPlatformFileDialogCall8)(const void *, int, int, QWindow *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall9)(const void *, int *);
typedef void (*CuteQQuickPlatformFileDialogCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQQuickPlatformFileDialogCall11)(const void *, int *);
typedef bool (*CuteQQuickPlatformFileDialogCall12)(const void *, const QUrl *, int *);
typedef const QVariant * (*CuteQQuickPlatformFileDialogCall13)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformFileDialogCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlatformFileDialogCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFileDialogCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFileDialogCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFileDialogCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFileDialogCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlatformFileDialogCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlatformFileDialog : public QQuickPlatformFileDialog {
public:
  using QQuickPlatformFileDialog::QQuickPlatformFileDialog;
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

  //  bool QQuickPlatformFileDialog::defaultNameFilterDisables() const
  bool defaultNameFilterDisables() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall0 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPlatformFileDialog::defaultNameFilterDisables();
  }

  //  void QQuickPlatformFileDialog::setDirectory(const QUrl &directory)
  void setDirectory(const QUrl &directory) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall1 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall1>(taken[1]);
      call(this, &directory, &handled);
      if (handled) return;
    }
    QQuickPlatformFileDialog::setDirectory(directory);
  }

  //  QUrl QQuickPlatformFileDialog::directory() const
  QUrl directory() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall2 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall2>(taken[2]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPlatformFileDialog::directory();
  }

  //  void QQuickPlatformFileDialog::selectFile(const QUrl &file)
  void selectFile(const QUrl &file) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall3 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall3>(taken[3]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QQuickPlatformFileDialog::selectFile(file);
  }

  //  void QQuickPlatformFileDialog::setFilter()
  void setFilter() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall4 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFileDialog::setFilter();
  }

  //  void QQuickPlatformFileDialog::selectNameFilter(const QString
  //      &filter)
  void selectNameFilter(const QString &filter) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall5 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall5>(taken[5]);
      call(this, &filter, &handled);
      if (handled) return;
    }
    QQuickPlatformFileDialog::selectNameFilter(filter);
  }

  //  QString QQuickPlatformFileDialog::selectedNameFilter() const
  QString selectedNameFilter() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall6 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickPlatformFileDialog::selectedNameFilter();
  }

  //  void QQuickPlatformFileDialog::exec()
  void exec() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall7 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFileDialog::exec();
  }

  //  bool QQuickPlatformFileDialog::show(Qt::WindowFlags flags,
  //      Qt::WindowModality modality, QWindow *parent)
  bool show(
      Qt::WindowFlags flags,
      Qt::WindowModality modality,
      QWindow *parent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall8 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall8>(taken[8]);
      bool given = call(this, static_cast<int>(flags.toInt()), static_cast<int>(modality), parent, &handled);
      if (handled) return given;
    }
    return QQuickPlatformFileDialog::show(flags, modality, parent);
  }

  //  void QQuickPlatformFileDialog::hide()
  void hide() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall9 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPlatformFileDialog::hide();
  }

  //  void QPlatformFileDialogHelper::selectMimeTypeFilter(const QString
  //      &filter)
  void selectMimeTypeFilter(const QString &filter) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall10 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall10>(taken[10]);
      call(this, &filter, &handled);
      if (handled) return;
    }
    QPlatformFileDialogHelper::selectMimeTypeFilter(filter);
  }

  //  QString QPlatformFileDialogHelper::selectedMimeTypeFilter() const
  QString selectedMimeTypeFilter() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall11 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall11>(taken[11]);
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
      CuteQQuickPlatformFileDialogCall12 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall12>(taken[12]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QPlatformFileDialogHelper::isSupportedUrl(url);
  }

  //  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformDialogHelper::StyleHint hint) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPlatformFileDialogCall13 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall13>(taken[13]);
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
      CuteQQuickPlatformFileDialogCall14 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall14>(taken[14]);
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
      CuteQQuickPlatformFileDialogCall15 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall15>(taken[15]);
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
      CuteQQuickPlatformFileDialogCall16 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall16>(taken[16]);
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
      CuteQQuickPlatformFileDialogCall17 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall17>(taken[17]);
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
      CuteQQuickPlatformFileDialogCall18 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall18>(taken[18]);
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
      CuteQQuickPlatformFileDialogCall19 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall19>(taken[19]);
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
      CuteQQuickPlatformFileDialogCall20 call = reinterpret_cast<CuteQQuickPlatformFileDialogCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlatformFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickPlatformFileDialog10metaObjectEv(
    const QQuickPlatformFileDialog *self) {
  return self->metaObject();
}

//  QString QQuickPlatformFileDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickPlatformFileDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlatformFileDialog::tr(s, c, n));
}

//  QQuickPlatformFileDialog::QQuickPlatformFileDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlatformFileDialog *ritual_ZN24QQuickPlatformFileDialogC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlatformFileDialog(parent);
}

//  QQuickPlatformFileDialog::~QQuickPlatformFileDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialogD1Ev(
    QQuickPlatformFileDialog *self) {
  delete self;
}

//  bool QQuickPlatformFileDialog::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPlatformFileDialog7isValidEv(
    const QQuickPlatformFileDialog *self) {
  return self->isValid();
}

//  bool QQuickPlatformFileDialog::defaultNameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPlatformFileDialog25defaultNameFilterDisablesEv(
    const QQuickPlatformFileDialog *self) {
  return self->defaultNameFilterDisables();
}

//  void QQuickPlatformFileDialog::setDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialog12setDirectoryERK4QUrl(
    QQuickPlatformFileDialog *self,
    const QUrl *directory) {
  self->setDirectory(*directory);
}

//  QUrl QQuickPlatformFileDialog::directory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QQuickPlatformFileDialog9directoryEv(
    const QQuickPlatformFileDialog *self) {
  return new QUrl(self->directory());
}

//  void QQuickPlatformFileDialog::selectFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialog10selectFileERK4QUrl(
    QQuickPlatformFileDialog *self,
    const QUrl *file) {
  self->selectFile(*file);
}

//  QList<QUrl> QQuickPlatformFileDialog::selectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK24QQuickPlatformFileDialog13selectedFilesEv(
    const QQuickPlatformFileDialog *self) {
  return new QList<QUrl>(self->selectedFiles());
}

//  void QQuickPlatformFileDialog::setFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialog9setFilterEv(
    QQuickPlatformFileDialog *self) {
  self->setFilter();
}

//  void QQuickPlatformFileDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialog16selectNameFilterERK7QString(
    QQuickPlatformFileDialog *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QString QQuickPlatformFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickPlatformFileDialog18selectedNameFilterEv(
    const QQuickPlatformFileDialog *self) {
  return new QString(self->selectedNameFilter());
}

//  void QQuickPlatformFileDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialog4execEv(
    QQuickPlatformFileDialog *self) {
  self->exec();
}

//  bool QQuickPlatformFileDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickPlatformFileDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformFileDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformFileDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPlatformFileDialog4hideEv(
    QQuickPlatformFileDialog *self) {
  self->hide();
}

//  QQuickFileDialogImpl *QQuickPlatformFileDialog::dialog() const
extern "C" Q_DECL_EXPORT
QQuickFileDialogImpl *ritual_ZNK24QQuickPlatformFileDialog6dialogEv(
    const QQuickPlatformFileDialog *self) {
  return self->dialog();
}

//  a Python function taken by a CuteQQuickPlatformFileDialog, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlatformFileDialog(
    QQuickPlatformFileDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlatformFileDialog *>(self)->take(key, call);
}

//  bool QQuickPlatformFileDialog::defaultNameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQuickPlatformFileDialog25defaultNameFilterDisablesEv(
    const QQuickPlatformFileDialog *self) {
  return self->QQuickPlatformFileDialog::defaultNameFilterDisables();
}

//  void QQuickPlatformFileDialog::setDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFileDialog12setDirectoryERK4QUrl(
    QQuickPlatformFileDialog *self,
    const QUrl *directory) {
  self->QQuickPlatformFileDialog::setDirectory(*directory);
}

//  QUrl QQuickPlatformFileDialog::directory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK24QQuickPlatformFileDialog9directoryEv(
    const QQuickPlatformFileDialog *self) {
  return new QUrl(self->QQuickPlatformFileDialog::directory());
}

//  void QQuickPlatformFileDialog::selectFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFileDialog10selectFileERK4QUrl(
    QQuickPlatformFileDialog *self,
    const QUrl *file) {
  self->QQuickPlatformFileDialog::selectFile(*file);
}

//  void QQuickPlatformFileDialog::setFilter()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFileDialog9setFilterEv(
    QQuickPlatformFileDialog *self) {
  self->QQuickPlatformFileDialog::setFilter();
}

//  void QQuickPlatformFileDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFileDialog16selectNameFilterERK7QString(
    QQuickPlatformFileDialog *self,
    const QString *filter) {
  self->QQuickPlatformFileDialog::selectNameFilter(*filter);
}

//  QString QQuickPlatformFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QQuickPlatformFileDialog18selectedNameFilterEv(
    const QQuickPlatformFileDialog *self) {
  return new QString(self->QQuickPlatformFileDialog::selectedNameFilter());
}

//  void QQuickPlatformFileDialog::exec()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFileDialog4execEv(
    QQuickPlatformFileDialog *self) {
  self->QQuickPlatformFileDialog::exec();
}

//  bool QQuickPlatformFileDialog::show(Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQuickPlatformFileDialog4showE6QFlagsIN2Qt10WindowTypeEENS1_14WindowModalityEP7QWindow(
    QQuickPlatformFileDialog *self,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return self->QQuickPlatformFileDialog::show(
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  void QQuickPlatformFileDialog::hide()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickPlatformFileDialog4hideEv(
    QQuickPlatformFileDialog *self) {
  self->QQuickPlatformFileDialog::hide();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
