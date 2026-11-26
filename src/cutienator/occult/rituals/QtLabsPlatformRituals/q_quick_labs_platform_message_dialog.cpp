//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtQml/qqmlinfo.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 59, as _ZN24QQuickLabsPlatformDialogC2EN14QPlatformTheme10DialogTypeEP7QObject
inline QQuickLabsPlatformDialog::QQuickLabsPlatformDialog(QPlatformTheme::DialogType type, QObject *parent)
    : QObject(parent),
      m_visible(false),
      m_complete(false),
      m_result(0),
      m_parentWindow(nullptr),
      m_flags(Qt::Dialog),
      m_modality(Qt::WindowModal),
      m_type(type),
      m_handle(nullptr)
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 72, as _ZN24QQuickLabsPlatformDialogD2Ev
inline QQuickLabsPlatformDialog::~QQuickLabsPlatformDialog()
{
    destroy();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 313, as _ZN31QQuickLabsPlatformMessageDialog8onCreateEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformMessageDialog::onCreate(QPlatformDialogHelper *dialog)
{
    if (QPlatformMessageDialogHelper *messageDialog = qobject_cast<QPlatformMessageDialogHelper *>(dialog)) {
        connect(messageDialog, &QPlatformMessageDialogHelper::clicked, this, &QQuickLabsPlatformMessageDialog::handleClick);
        messageDialog->setOptions(m_options);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 321, as _ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper *dialog)
{
    m_options->setWindowTitle(title());
    if (QPlatformMessageDialogHelper *messageDialog = qobject_cast<QPlatformMessageDialogHelper *>(dialog))
        messageDialog->setOptions(m_options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 328, as _ZN31QQuickLabsPlatformMessageDialog11handleClickEN21QPlatformDialogHelper14StandardButtonE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformMessageDialog::handleClick(QPlatformDialogHelper::StandardButton button)
{
    done(button);
    emit clicked(button);

    switch (button) {
    case QPlatformDialogHelper::Ok: emit okClicked(); break;
    case QPlatformDialogHelper::Save: emit saveClicked(); break;
    case QPlatformDialogHelper::SaveAll: emit saveAllClicked(); break;
    case QPlatformDialogHelper::Open: emit openClicked(); break;
    case QPlatformDialogHelper::Yes: emit yesClicked(); break;
    case QPlatformDialogHelper::YesToAll: emit yesToAllClicked(); break;
    case QPlatformDialogHelper::No: emit noClicked(); break;
    case QPlatformDialogHelper::NoToAll: emit noToAllClicked(); break;
    case QPlatformDialogHelper::Abort: emit abortClicked(); break;
    case QPlatformDialogHelper::Retry: emit retryClicked(); break;
    case QPlatformDialogHelper::Ignore: emit ignoreClicked(); break;
    case QPlatformDialogHelper::Close: emit closeClicked(); break;
    case QPlatformDialogHelper::Cancel: emit cancelClicked(); break;
    case QPlatformDialogHelper::Discard: emit discardClicked(); break;
    case QPlatformDialogHelper::Help: emit helpClicked(); break;
    case QPlatformDialogHelper::Apply: emit applyClicked(); break;
    case QPlatformDialogHelper::Reset: emit resetClicked(); break;
    case QPlatformDialogHelper::RestoreDefaults: emit restoreDefaultsClicked(); break;
    default: qmlWarning(this) << "unknown button" << int(button); break;
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 122, as _ZNK24QQuickLabsPlatformDialog5titleEv
inline QString QQuickLabsPlatformDialog::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 212, as _ZNK31QQuickLabsPlatformMessageDialog4textEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformMessageDialog::text() const
{
    return m_options->text();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 235, as _ZNK31QQuickLabsPlatformMessageDialog15informativeTextEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformMessageDialog::informativeText() const
{
    return m_options->informativeText();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 256, as _ZNK31QQuickLabsPlatformMessageDialog12detailedTextEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformMessageDialog::detailedText() const
{
    return m_options->detailedText();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 299, as _ZNK31QQuickLabsPlatformMessageDialog7buttonsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QPlatformDialogHelper::StandardButtons QQuickLabsPlatformMessageDialog::buttons() const
{
    return m_options->standardButtons();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformMessageDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformMessageDialog : QQuickLabsPlatformMessageDialog {
  using QQuickLabsPlatformMessageDialog::onShow;
};

//  const QMetaObject *QQuickLabsPlatformMessageDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickLabsPlatformMessageDialog10metaObjectEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformMessageDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickLabsPlatformMessageDialog11qt_metacastEPKc(
    QQuickLabsPlatformMessageDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformMessageDialog::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickLabsPlatformMessageDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformMessageDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QMetaObject
//      *QQuickLabsPlatformMessageDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN31QQuickLabsPlatformMessageDialog20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformMessageDialog::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformMessageDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformMessageDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformMessageDialog::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickLabsPlatformMessageDialog4textEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return new QString(self->text());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformMessageDialog::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickLabsPlatformMessageDialog15informativeTextEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return new QString(self->informativeText());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformMessageDialog::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickLabsPlatformMessageDialog12detailedTextEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return new QString(self->detailedText());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QPlatformDialogHelper::StandardButtons
//      QQuickLabsPlatformMessageDialog::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQuickLabsPlatformMessageDialog7buttonsEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return static_cast<int>(self->buttons().toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  void QQuickLabsPlatformMessageDialog::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog11textChangedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::informativeTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog22informativeTextChangedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "informativeTextChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "informativeTextChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::detailedTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog19detailedTextChangedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "detailedTextChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "detailedTextChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::buttonsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog14buttonsChangedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "buttonsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "buttonsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::clicked(QPlatformDialogHelper::Stan
//      dardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog7clickedEN21QPlatformDialogHelper14StandardButtonE(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper::StandardButton button) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clicked(QPlatformDialogHelper::StandardButton)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clicked(QPlatformDialogHelper::StandardButton)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&button)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::okClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog9okClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "okClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "okClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::saveClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog11saveClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "saveClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "saveClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::saveAllClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog14saveAllClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "saveAllClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "saveAllClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::openClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog11openClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "openClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "openClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::yesClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog10yesClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yesClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yesClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::yesToAllClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog15yesToAllClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yesToAllClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yesToAllClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::noClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog9noClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "noClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "noClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::noToAllClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog14noToAllClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "noToAllClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "noToAllClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::abortClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog12abortClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "abortClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "abortClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::retryClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog12retryClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "retryClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "retryClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::ignoreClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog13ignoreClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ignoreClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ignoreClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::closeClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog12closeClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "closeClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "closeClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::cancelClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog13cancelClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cancelClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cancelClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::discardClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog14discardClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "discardClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "discardClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::helpClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog11helpClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "helpClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "helpClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::applyClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog12applyClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "applyClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "applyClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::resetClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog12resetClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resetClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resetClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::restoreDefaultsClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog22restoreDefaultsClickedEv(
    QQuickLabsPlatformMessageDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "restoreDefaultsClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "restoreDefaultsClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMessageDialog::onCreate(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickLabsPlatformMessageDialog::handleClick(QPlatformDialogHelper::
//      StandardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog11handleClickEN21QPlatformDialogHelper14StandardButtonE(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper::StandardButton button) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMessageDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleClick(QPlatformDialogHelper::StandardButton)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleClick(QPlatformDialogHelper::StandardButton)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&button)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformMessageDialog *>(self)->OwnQQuickLabsPlatformMessageDialog::onShow(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)
