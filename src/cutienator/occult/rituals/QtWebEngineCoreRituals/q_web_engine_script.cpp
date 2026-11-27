//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginescript.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginescript.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  QWebEngineScript::QWebEngineScript()
extern "C" Q_DECL_EXPORT
QWebEngineScript *ritual_ZN16QWebEngineScriptC1Ev() {
  return new QWebEngineScript();
}

//  QWebEngineScript::QWebEngineScript(const QWebEngineScript &other)
extern "C" Q_DECL_EXPORT
QWebEngineScript *ritual_ZN16QWebEngineScriptC1ERKS_(
    const QWebEngineScript *other) {
  return new QWebEngineScript(*other);
}

//  QWebEngineScript::~QWebEngineScript()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScriptD1Ev(QWebEngineScript *self) {
  delete self;
}

//  QWebEngineScript &QWebEngineScript::operator=(const QWebEngineScript
//      &other)
extern "C" Q_DECL_EXPORT
QWebEngineScript *ritual_ZN16QWebEngineScriptaSERKS_(
    QWebEngineScript *self,
    const QWebEngineScript *other) {
  return &(self->operator=(*other));
}

//  QString QWebEngineScript::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QWebEngineScript4nameEv(const QWebEngineScript *self) {
  return new QString(self->name());
}

//  void QWebEngineScript::setName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript7setNameERK7QString(
    QWebEngineScript *self,
    const QString *a0) {
  self->setName(*a0);
}

//  QUrl QWebEngineScript::sourceUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QWebEngineScript9sourceUrlEv(
    const QWebEngineScript *self) {
  return new QUrl(self->sourceUrl());
}

//  void QWebEngineScript::setSourceUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript12setSourceUrlERK4QUrl(
    QWebEngineScript *self,
    const QUrl *url) {
  self->setSourceUrl(*url);
}

//  QString QWebEngineScript::sourceCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QWebEngineScript10sourceCodeEv(
    const QWebEngineScript *self) {
  return new QString(self->sourceCode());
}

//  void QWebEngineScript::setSourceCode(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript13setSourceCodeERK7QString(
    QWebEngineScript *self,
    const QString *a0) {
  self->setSourceCode(*a0);
}

//  InjectionPoint QWebEngineScript::injectionPoint() const
extern "C" Q_DECL_EXPORT
QWebEngineScript::InjectionPoint ritual_ZNK16QWebEngineScript14injectionPointEv(
    const QWebEngineScript *self) {
  return self->injectionPoint();
}

//  void QWebEngineScript::setInjectionPoint(InjectionPoint a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript17setInjectionPointENS_14InjectionPointE(
    QWebEngineScript *self,
    QWebEngineScript::InjectionPoint a0) {
  self->setInjectionPoint(a0);
}

//  quint32 QWebEngineScript::worldId() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QWebEngineScript7worldIdEv(
    const QWebEngineScript *self) {
  return self->worldId();
}

//  void QWebEngineScript::setWorldId(quint32 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript10setWorldIdEj(
    QWebEngineScript *self,
    quint32 a0) {
  self->setWorldId(a0);
}

//  bool QWebEngineScript::runsOnSubFrames() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebEngineScript15runsOnSubFramesEv(
    const QWebEngineScript *self) {
  return self->runsOnSubFrames();
}

//  void QWebEngineScript::setRunsOnSubFrames(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript18setRunsOnSubFramesEb(
    QWebEngineScript *self,
    bool on) {
  self->setRunsOnSubFrames(on);
}

//  bool QWebEngineScript::operator==(const QWebEngineScript &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebEngineScripteqERKS_(
    const QWebEngineScript *self,
    const QWebEngineScript *other) {
  return self->operator==(*other);
}

//  bool QWebEngineScript::operator!=(const QWebEngineScript &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebEngineScriptneERKS_(
    const QWebEngineScript *self,
    const QWebEngineScript *other) {
  return self->operator!=(*other);
}

//  void QWebEngineScript::swap(QWebEngineScript &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebEngineScript4swapERS_(
    QWebEngineScript *self,
    QWebEngineScript *other) {
  self->swap(*other);
}

//  QWebEngineScript::QWebEngineScript(const QtWebEngineCore::UserScript &a0)
extern "C" Q_DECL_EXPORT
QWebEngineScript *ritual_ZN16QWebEngineScriptC1ERKN15QtWebEngineCore10UserScriptE(
    const QtWebEngineCore::UserScript *a0) {
  return new QWebEngineScript(*a0);
}

//  QList<QWebEngineScript>::QList()
extern "C" Q_DECL_EXPORT
QList<QWebEngineScript> *ritual_list_make_QWebEngineScript() {
  return new QList<QWebEngineScript>();
}

//  void QList<QWebEngineScript>::append(const QWebEngineScript &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWebEngineScript(
    QList<QWebEngineScript> *self,
    const QWebEngineScript *element) {
  self->append(*element);
}

//  qsizetype QList<QWebEngineScript>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWebEngineScript(
    const QList<QWebEngineScript> *self) {
  return self->size();
}

//  const QWebEngineScript &QList<QWebEngineScript>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWebEngineScript *ritual_list_at_QWebEngineScript(
    const QList<QWebEngineScript> *self,
    long long index) {
  return new QWebEngineScript(self->at(index));
}

//  QList<QWebEngineScript>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWebEngineScript(QList<QWebEngineScript> *self) {
  delete self;
}
