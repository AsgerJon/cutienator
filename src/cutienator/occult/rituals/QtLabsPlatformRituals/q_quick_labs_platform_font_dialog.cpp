//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfontdialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfontdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtLabsPlatform/private/qquicklabsplatformfontdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 77, as _ZNK24QQuickLabsPlatformDialog6handleEv
inline QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 155, as _ZNK28QQuickLabsPlatformFontDialog15useNativeDialogEv
#if QT_DEPRECATED_SINCE(6, 9)
inline bool QQuickLabsPlatformFontDialog::useNativeDialog() const
{
    return QQuickLabsPlatformDialog::useNativeDialog()
            && !m_options->testOption(QFontDialogOptions::DontUseNativeDialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 161, as _ZN28QQuickLabsPlatformFontDialog8onCreateEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFontDialog::onCreate(QPlatformDialogHelper *dialog)
{
    if (QPlatformFontDialogHelper *fontDialog = qobject_cast<QPlatformFontDialogHelper *>(dialog)) {
        connect(fontDialog, &QPlatformFontDialogHelper::currentFontChanged, this, &QQuickLabsPlatformFontDialog::currentFontChanged);
        fontDialog->setOptions(m_options);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 169, as _ZN28QQuickLabsPlatformFontDialog6onShowEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFontDialog::onShow(QPlatformDialogHelper *dialog)
{
    m_options->setWindowTitle(title());
    if (QPlatformFontDialogHelper *fontDialog = qobject_cast<QPlatformFontDialogHelper *>(dialog))
        fontDialog->setOptions(m_options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 176, as _ZN28QQuickLabsPlatformFontDialog6acceptEv
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFontDialog::accept()
{
    setFont(currentFont());
    QQuickLabsPlatformDialog::accept();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 342, as _ZNK24QQuickLabsPlatformDialog15useNativeDialogEv
inline bool QQuickLabsPlatformDialog::useNativeDialog() const
{
    return !QCoreApplication::testAttribute(Qt::AA_DontUseNativeDialogs)
            && QGuiApplicationPrivate::platformTheme()->usePlatformNativeDialog(m_type);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 122, as _ZNK24QQuickLabsPlatformDialog5titleEv
inline QString QQuickLabsPlatformDialog::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 268, as _ZN24QQuickLabsPlatformDialog6acceptEv
inline void QQuickLabsPlatformDialog::accept()
{
    done(Accepted);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 88, as _ZN28QQuickLabsPlatformFontDialog7setFontERK5QFont
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFontDialog::setFont(const QFont &font)
{
    if (m_font == font)
        return;

    m_font = font;
    setCurrentFont(font);
    emit fontChanged();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 83, as _ZNK28QQuickLabsPlatformFontDialog4fontEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QFont QQuickLabsPlatformFontDialog::font() const
{
    return m_font;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 109, as _ZNK28QQuickLabsPlatformFontDialog11currentFontEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QFont QQuickLabsPlatformFontDialog::currentFont() const
{
    if (QPlatformFontDialogHelper *fontDialog = qobject_cast<QPlatformFontDialogHelper *>(handle()))
        return fontDialog->currentFont();
    return m_currentFont;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 116, as _ZN28QQuickLabsPlatformFontDialog14setCurrentFontERK5QFont
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFontDialog::setCurrentFont(const QFont &font)
{
    if (QPlatformFontDialogHelper *fontDialog = qobject_cast<QPlatformFontDialogHelper *>(handle()))
        fontDialog->setCurrentFont(font);
    m_currentFont = font;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfontdialog.cpp, line 141, as _ZNK28QQuickLabsPlatformFontDialog7optionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QFontDialogOptions::FontDialogOptions QQuickLabsPlatformFontDialog::options() const
{
    return m_options->options();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformFontDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformFontDialog : QQuickLabsPlatformFontDialog {
  using QQuickLabsPlatformFontDialog::useNativeDialog;
  using QQuickLabsPlatformFontDialog::onShow;
};

//  const QMetaObject *QQuickLabsPlatformFontDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickLabsPlatformFontDialog10metaObjectEv(
    const QQuickLabsPlatformFontDialog *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformFontDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickLabsPlatformFontDialog11qt_metacastEPKc(
    QQuickLabsPlatformFontDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformFontDialog::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickLabsPlatformFontDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformFontDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QMetaObject *QQuickLabsPlatformFontDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN28QQuickLabsPlatformFontDialog20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformFontDialog::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformFontDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformFontDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QFont QQuickLabsPlatformFontDialog::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK28QQuickLabsPlatformFontDialog4fontEv(
    const QQuickLabsPlatformFontDialog *self) {
  return new QFont(self->font());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QFont QQuickLabsPlatformFontDialog::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK28QQuickLabsPlatformFontDialog11currentFontEv(
    const QQuickLabsPlatformFontDialog *self) {
  return new QFont(self->currentFont());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFontDialog::setCurrentFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog14setCurrentFontERK5QFont(
    QQuickLabsPlatformFontDialog *self,
    const QFont *font) {
  self->setCurrentFont(*font);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QFontDialogOptions::FontDialogOptions
//      QQuickLabsPlatformFontDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickLabsPlatformFontDialog7optionsEv(
    const QQuickLabsPlatformFontDialog *self) {
  return static_cast<int>(self->options().toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  void QQuickLabsPlatformFontDialog::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog11fontChangedEv(
    QQuickLabsPlatformFontDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFontDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fontChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fontChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFontDialog::currentFontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog18currentFontChangedEv(
    QQuickLabsPlatformFontDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFontDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentFontChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentFontChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFontDialog::optionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog14optionsChangedEv(
    QQuickLabsPlatformFontDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFontDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "optionsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "optionsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QQuickLabsPlatformFontDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickLabsPlatformFontDialog15useNativeDialogEv(
    const QQuickLabsPlatformFontDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickLabsPlatformFontDialog::onCreate(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformFontDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformFontDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformFontDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickLabsPlatformFontDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFontDialog6acceptEv(
    QQuickLabsPlatformFontDialog *self) {
  self->accept();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  bool QQuickLabsPlatformFontDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QQuickLabsPlatformFontDialog15useNativeDialogEv(
    const QQuickLabsPlatformFontDialog *self) {
  return static_cast<const OwnQQuickLabsPlatformFontDialog *>(self)->OwnQQuickLabsPlatformFontDialog::useNativeDialog();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFontDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickLabsPlatformFontDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformFontDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformFontDialog *>(self)->OwnQQuickLabsPlatformFontDialog::onShow(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)
