//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/qlist.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 586, as local:qquicklabsplatformfiledialog.cpp:extractName
#if QT_DEPRECATED_SINCE(6, 9)
static QString extractName(const QString &filter)
{
    return filter.left(filter.indexOf(QLatin1Char('(')) - 1);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 591, as local:qquicklabsplatformfiledialog.cpp:extractExtension
#if QT_DEPRECATED_SINCE(6, 9)
static QString extractExtension(QStringView filter)
{
    return filter.mid(filter.indexOf(QLatin1Char('.')) + 1).toString();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 596, as local:qquicklabsplatformfiledialog.cpp:extractExtensions
#if QT_DEPRECATED_SINCE(6, 9)
static QStringList extractExtensions(QStringView filter)
{
    QStringList extensions;
    const int from = filter.indexOf(QLatin1Char('('));
    const int to = filter.lastIndexOf(QLatin1Char(')')) - 1;
    if (from >= 0 && from < to) {
        const QStringView ref = filter.mid(from + 1, to - from);
        const QList<QStringView> exts = ref.split(QLatin1Char(' '), Qt::SkipEmptyParts);
        for (const QStringView &ref : exts)
            extensions += extractExtension(ref);
    }

    return extensions;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 552, as _ZNK32QQuickLabsPlatformFileNameFilter5indexEv
#if QT_DEPRECATED_SINCE(6, 9)
inline int QQuickLabsPlatformFileNameFilter::index() const
{
    return m_index;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 566, as _ZNK32QQuickLabsPlatformFileNameFilter4nameEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileNameFilter::name() const
{
    return m_name;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 571, as _ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::extensions() const
{
    return m_extensions;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 576, as _ZNK32QQuickLabsPlatformFileNameFilter7optionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QSharedPointer<QFileDialogOptions> QQuickLabsPlatformFileNameFilter::options() const
{
    return m_options;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 581, as _ZN32QQuickLabsPlatformFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::setOptions(const QSharedPointer<QFileDialogOptions> &options)
{
    m_options = options;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 631, as _ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
{
    return m_options ? m_options->nameFilters() : QStringList();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 636, as _ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
{
    return m_options ? m_options->nameFilters().value(index) : QString();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLabsPlatformFileNameFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickLabsPlatformFileNameFilter10metaObjectEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformFileNameFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickLabsPlatformFileNameFilter11qt_metacastEPKc(
    QQuickLabsPlatformFileNameFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformFileNameFilter::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickLabsPlatformFileNameFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformFileNameFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickLabsPlatformFileNameFilter::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter22qt_qmlMarker_anonymousEv(
    QQuickLabsPlatformFileNameFilter *self) {
  self->qt_qmlMarker_anonymous();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  int QQuickLabsPlatformFileNameFilter::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuickLabsPlatformFileNameFilter5indexEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return self->index();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformFileNameFilter4nameEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QString(self->name());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileNameFilter::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QList<QString>(self->extensions());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QSharedPointer<QFileDialogOptions>
//      QQuickLabsPlatformFileNameFilter::options() const
extern "C" Q_DECL_EXPORT
QSharedPointer<QFileDialogOptions> *ritual_ZNK32QQuickLabsPlatformFileNameFilter7optionsEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QSharedPointer<QFileDialogOptions>(self->options());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileNameFilter::setOptions(const
//      QSharedPointer<QFileDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE(
    QQuickLabsPlatformFileNameFilter *self,
    const QSharedPointer<QFileDialogOptions> *options) {
  self->setOptions(*options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  void QQuickLabsPlatformFileNameFilter::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter11nameChangedERK7QString(
    QQuickLabsPlatformFileNameFilter *self,
    const QString *name) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileNameFilter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "nameChanged(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "nameChanged(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(name)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileNameFilter::extensionsChanged(const
//      QStringList &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter17extensionsChangedERK5QListI7QStringE(
    QQuickLabsPlatformFileNameFilter *self,
    const QList<QString> *extensions) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileNameFilter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "extensionsChanged(const QStringList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "extensionsChanged(const QStringList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(extensions)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QList<QString>(self->nameFilters());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi(
    const QQuickLabsPlatformFileNameFilter *self,
    int index) {
  return new QString(self->nameFilter(index));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  a QSharedPointer<QFileDialogOptions> a ritual of
//      QQuickLabsPlatformFileNameFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickLabsPlatformFileNameFilter__QSharedPointer_QFileDialogOptions(
    QSharedPointer<QFileDialogOptions> *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 9)
