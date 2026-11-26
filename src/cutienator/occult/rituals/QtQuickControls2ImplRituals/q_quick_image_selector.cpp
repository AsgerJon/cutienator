//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickimageselector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickimageselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/private/qquickimageselector_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qdir.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qfileselector.h>
#include <QtCore/qloggingcategory.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlfile.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 22, as local:qquickimageselector.cpp:DEFAULT_CACHE
Q_STATIC_LOGGING_CATEGORY(lcQtQuickControlsImageSelector, "qt.quick.controls.imageselector")

static const int DEFAULT_CACHE = 500;

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 26, as local:qquickimageselector.cpp:cacheSize
static inline int cacheSize()
{
    static bool ok = false;
    static const int size = qEnvironmentVariableIntValue("QT_QUICK_CONTROLS_IMAGESELECTOR_CACHE", &ok);
    return ok ? size : DEFAULT_CACHE;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 35, as local:qquickimageselector.cpp:permutations
static QList<QStringList> permutations(const QStringList &input, int count = -1)
{
    if (count == -1)
        count = input.size();

    QList<QStringList> output;
    for (int i = 0; i < input.size(); ++i) {
        QStringList sub = input.mid(i, count);

        if (count > 1) {
            if (i + count > input.size())
                sub += input.mid(0, count - i + 1);

            std::sort(sub.begin(), sub.end());
            do {
                if (!sub.isEmpty())
                    output += sub;
            } while (std::next_permutation(sub.begin(), sub.end()));
        } else {
            output += sub;
        }

        if (count == input.size())
            break;
    }

    if (count > 1)
        output += permutations(input, --count);

    return output;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 67, as local:qquickimageselector.cpp:findFile
static QString findFile(const QDir &dir, const QString &baseName, const QStringList &extensions)
{
    for (const QString &ext : extensions) {
        QString filePath = dir.filePath(baseName + QLatin1Char('.') + ext);
        if (QFile::exists(filePath))
            return QFileSelector().select(filePath);
    }
    // return an empty string to indicate that the lookup has been done
    // even if no matching asset was found
    return QLatin1String("");
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 171, as _ZN19QQuickImageSelector5writeERK8QVariant
inline void QQuickImageSelector::write(const QVariant &value)
{
    setUrl(value.toUrl());
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 176, as _ZN19QQuickImageSelector9setTargetERK12QQmlProperty
inline void QQuickImageSelector::setTarget(const QQmlProperty &property)
{
    m_property = property;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 181, as _ZN19QQuickImageSelector10classBeginEv
inline void QQuickImageSelector::classBegin()
{
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 185, as _ZN19QQuickImageSelector17componentCompleteEv
inline void QQuickImageSelector::componentComplete()
{
    setUrl(m_property.read().toUrl());
    m_complete = true;
    updateSource();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 85, as _ZNK19QQuickImageSelector6sourceEv
inline QUrl QQuickImageSelector::source() const
{
    return m_source;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 101, as _ZNK19QQuickImageSelector4nameEv
inline QString QQuickImageSelector::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 116, as _ZNK19QQuickImageSelector4pathEv
inline QString QQuickImageSelector::path() const
{
    return m_path;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 131, as _ZNK19QQuickImageSelector6statesEv
inline QVariantList QQuickImageSelector::states() const
{
    return m_allStates;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 146, as _ZNK19QQuickImageSelector9separatorEv
inline QString QQuickImageSelector::separator() const
{
    return m_separator;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 161, as _ZNK19QQuickImageSelector5cacheEv
inline bool QQuickImageSelector::cache() const
{
    return m_cache;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 166, as _ZN19QQuickImageSelector8setCacheEb
inline void QQuickImageSelector::setCache(bool cache)
{
    m_cache = cache;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 198, as _ZNK19QQuickImageSelector8cacheKeyEv
inline QString QQuickImageSelector::cacheKey() const
{
    if (!m_cache)
        return QString();

    return m_path + m_name + m_activeStates.join(m_separator);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 269, as _ZN19QQuickImageSelector18updateActiveStatesEv
inline bool QQuickImageSelector::updateActiveStates()
{
    QStringList active;
    for (const QVariant &v : std::as_const(m_allStates)) {
        const QVariantMap state = v.toMap();
        if (state.isEmpty())
            continue;
        auto it = state.begin();
        if (it.value().toBool())
            active += it.key();
    }

    if (m_activeStates == active)
        return false;

    m_activeStates = active;
    return true;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickimageselector.cpp, line 288, as _ZNK19QQuickImageSelector14calculateScoreERK5QListI7QStringE
inline int QQuickImageSelector::calculateScore(const QStringList &states) const
{
    int score = 0;
    for (int i = 0; i < states.size(); ++i)
        score += (m_activeStates.size() - m_activeStates.indexOf(states.at(i))) << 1;
    return score;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickImageSelector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickImageSelector : QQuickImageSelector {
  using QQuickImageSelector::classBegin;
};

//  const QMetaObject *QQuickImageSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickImageSelector10metaObjectEv(
    const QQuickImageSelector *self) {
  return self->metaObject();
}

//  void *QQuickImageSelector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickImageSelector11qt_metacastEPKc(
    QQuickImageSelector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickImageSelector::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickImageSelector11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickImageSelector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QUrl QQuickImageSelector::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuickImageSelector6sourceEv(
    const QQuickImageSelector *self) {
  return new QUrl(self->source());
}

//  QString QQuickImageSelector::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickImageSelector4nameEv(
    const QQuickImageSelector *self) {
  return new QString(self->name());
}

//  QString QQuickImageSelector::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickImageSelector4pathEv(
    const QQuickImageSelector *self) {
  return new QString(self->path());
}

//  QVariantList QQuickImageSelector::states() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK19QQuickImageSelector6statesEv(
    const QQuickImageSelector *self) {
  return new QList<QVariant>(self->states());
}

//  QString QQuickImageSelector::separator() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickImageSelector9separatorEv(
    const QQuickImageSelector *self) {
  return new QString(self->separator());
}

//  bool QQuickImageSelector::cache() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickImageSelector5cacheEv(
    const QQuickImageSelector *self) {
  return self->cache();
}

//  void QQuickImageSelector::setCache(bool cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageSelector8setCacheEb(
    QQuickImageSelector *self,
    bool cache) {
  self->setCache(cache);
}

//  void QQuickImageSelector::write(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageSelector5writeERK8QVariant(
    QQuickImageSelector *self,
    const QVariant *value) {
  self->write(*value);
}

//  void QQuickImageSelector::setTarget(const QQmlProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageSelector9setTargetERK12QQmlProperty(
    QQuickImageSelector *self,
    const QQmlProperty *property) {
  self->setTarget(*property);
}

//  void QQuickImageSelector::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageSelector13sourceChangedEv(
    QQuickImageSelector *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickImageSelector")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickImageSelector::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageSelector10classBeginEv(
    QQuickImageSelector *self) {
  self->classBegin();
}

//  void QQuickImageSelector::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageSelector17componentCompleteEv(
    QQuickImageSelector *self) {
  self->componentComplete();
}

//  QStringList QQuickImageSelector::fileExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QQuickImageSelector14fileExtensionsEv(
    const QQuickImageSelector *self) {
  return new QList<QString>(self->fileExtensions());
}

//  QString QQuickImageSelector::cacheKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickImageSelector8cacheKeyEv(
    const QQuickImageSelector *self) {
  return new QString(self->cacheKey());
}

//  bool QQuickImageSelector::updateActiveStates()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickImageSelector18updateActiveStatesEv(
    QQuickImageSelector *self) {
  return self->updateActiveStates();
}

//  int QQuickImageSelector::calculateScore(const QStringList &states) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickImageSelector14calculateScoreERK5QListI7QStringE(
    const QQuickImageSelector *self,
    const QList<QString> *states) {
  return self->calculateScore(*states);
}

//  QQuickImageSelector as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickImageSelector_QQmlParserStatus(
    QQuickImageSelector *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  QQuickImageSelector as the QQmlPropertyValueInterceptor it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyValueInterceptor *ritual_cast_QQuickImageSelector_QQmlPropertyValueInterceptor(
    QQuickImageSelector *self) {
  return static_cast<QQmlPropertyValueInterceptor *>(self);
}

//  void QQuickImageSelector::setTarget(const QQmlProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageSelector9setTargetERK12QQmlProperty(
    QQuickImageSelector *self,
    const QQmlProperty *property) {
  self->QQuickImageSelector::setTarget(*property);
}

//  void QQuickImageSelector::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickImageSelector10classBeginEv(
    QQuickImageSelector *self) {
  static_cast<OwnQQuickImageSelector *>(self)->OwnQQuickImageSelector::classBegin();
}
