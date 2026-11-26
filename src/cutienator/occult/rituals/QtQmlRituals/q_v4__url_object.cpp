//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4urlobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtCore/QUrl>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 53, as _ZN3QV49UrlObject7setHashERK7QString
namespace QV4 {
inline bool UrlObject::setHash(const QString &hash)
{
    return updateUrl([&](QUrl *url) {
        url->setFragment(hash.startsWith(QLatin1Char('#')) ? hash.mid(1) : hash);
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 67, as _ZN3QV49UrlObject7setHostERK7QString
namespace QV4 {
inline bool UrlObject::setHost(const QString &host)
{
    return updateUrl([&](QUrl *url) {
        qsizetype colon = host.indexOf(QLatin1Char(':'));
        if (colon == -1) {
            url->setHost(host);
            url->setPort(-1);
        } else {
            url->setHost(host.left(colon));
            url->setPort(QStringView(host).mid(colon + 1).toInt());
        }
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 60, as _ZN3QV49UrlObject11setHostnameERK7QString
namespace QV4 {
inline bool UrlObject::setHostname(const QString &hostName)
{
    return updateUrl([&](QUrl *url) {
        url->setHost(hostName);
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 81, as _ZN3QV49UrlObject7setHrefERK7QString
namespace QV4 {
inline bool UrlObject::setHref(const QString &href)
{
    QUrl replacement(href);
    if (!replacement.isValid() || replacement.isRelative())
        return false;

    d()->setUrl(std::move(replacement));
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 96, as _ZN3QV49UrlObject11setPasswordERK7QString
namespace QV4 {
inline bool UrlObject::setPassword(const QString &password)
{
    return updateUrl([&](QUrl *url) {
        url->setPassword(password);
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 103, as _ZN3QV49UrlObject11setPathnameERK7QString
namespace QV4 {
inline bool UrlObject::setPathname(const QString &pathname)
{
    return updateUrl([&](QUrl *url) {
        url->setPath(pathname);
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 110, as _ZN3QV49UrlObject7setPortERK7QString
namespace QV4 {
inline bool UrlObject::setPort(const QString &port)
{
    return updateUrl([&](QUrl *url) {
        url->setPort(port.isEmpty() ? -1 : port.toInt());
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 117, as _ZN3QV49UrlObject11setProtocolERK7QString
namespace QV4 {
inline bool UrlObject::setProtocol(const QString &protocolOrScheme)
{
    // If there is one or several ':' in the protocolOrScheme,
    // everything from the first colon is removed.

    return updateUrl([&](QUrl *url) {
        const qsizetype colon = protocolOrScheme.indexOf(QLatin1Char(':'));
        url->setScheme(colon == -1 ? protocolOrScheme : protocolOrScheme.left(colon));
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 155, as _ZNK3QV49UrlObject6searchEv
namespace QV4 {
inline QString UrlObject::search() const
{
    const QUrl url = d()->url();
    if (!url.hasQuery() || url.query().isEmpty())
        return QString();

    constexpr auto options = QUrl::ComponentFormattingOption::EncodeSpaces
            | QUrl::ComponentFormattingOption::EncodeUnicode
            | QUrl::ComponentFormattingOption::EncodeReserved;
    return QLatin1Char('?') + url.query(options);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 128, as _ZN3QV49UrlObject9setSearchERK7QString
namespace QV4 {
inline bool UrlObject::setSearch(const QString &search)
{
    return updateUrl([&](QUrl *url) {
        if (search.startsWith(QLatin1Char('?'))) {
            url->setQuery(search.mid(1));
            return;
        }

        if (search.isEmpty()) {
            // In JS, setting an empty query removes the '?' as well. QUrl only does that for a
            // null QString. The way to get a lone '?' in JS is to set the search property to "?".
            // That is why this is in the else branch.
            url->setQuery(QString()); // it's null now
            return;
        }

        url->setQuery(search);
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 148, as _ZN3QV49UrlObject11setUsernameERK7QString
namespace QV4 {
inline bool UrlObject::setUsername(const QString &username)
{
    return updateUrl([&](QUrl *url) {
        url->setUserName(username);
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 91, as _ZN3QV49UrlObject6setUrlERK4QUrl
namespace QV4 {
inline void UrlObject::setUrl(const QUrl &url)
{
    d()->setUrl(QUrl(url));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::UrlObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49UrlObject10__dataTestEv(QV4::UrlObject *self) {
  self->__dataTest();
}

//  QV4::Heap::UrlObject *QV4::UrlObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZNK3QV49UrlObject11d_uncheckedEv(
    const QV4::UrlObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::UrlObject *QV4::UrlObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZNK3QV49UrlObject1dEv(
    const QV4::UrlObject *self) {
  return self->d();
}

//  void QV4::UrlObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49UrlObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::UrlObject::virtualDestroy(b);
}

//  QV4::Object *QV4::UrlObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV49UrlObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::UrlObject::defaultPrototype(e);
}

//  QString QV4::UrlObject::hash() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4hashEv(const QV4::UrlObject *self) {
  return new QString(self->hash());
}

//  bool QV4::UrlObject::setHash(const QString &hash)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject7setHashERK7QString(
    QV4::UrlObject *self,
    const QString *hash) {
  return self->setHash(*hash);
}

//  QString QV4::UrlObject::host() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4hostEv(const QV4::UrlObject *self) {
  return new QString(self->host());
}

//  bool QV4::UrlObject::setHost(const QString &host)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject7setHostERK7QString(
    QV4::UrlObject *self,
    const QString *host) {
  return self->setHost(*host);
}

//  QString QV4::UrlObject::hostname() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8hostnameEv(const QV4::UrlObject *self) {
  return new QString(self->hostname());
}

//  bool QV4::UrlObject::setHostname(const QString &hostname)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject11setHostnameERK7QString(
    QV4::UrlObject *self,
    const QString *hostname) {
  return self->setHostname(*hostname);
}

//  QString QV4::UrlObject::href() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4hrefEv(const QV4::UrlObject *self) {
  return new QString(self->href());
}

//  bool QV4::UrlObject::setHref(const QString &href)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject7setHrefERK7QString(
    QV4::UrlObject *self,
    const QString *href) {
  return self->setHref(*href);
}

//  QString QV4::UrlObject::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject6originEv(const QV4::UrlObject *self) {
  return new QString(self->origin());
}

//  QString QV4::UrlObject::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8passwordEv(const QV4::UrlObject *self) {
  return new QString(self->password());
}

//  bool QV4::UrlObject::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject11setPasswordERK7QString(
    QV4::UrlObject *self,
    const QString *password) {
  return self->setPassword(*password);
}

//  QString QV4::UrlObject::pathname() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8pathnameEv(const QV4::UrlObject *self) {
  return new QString(self->pathname());
}

//  bool QV4::UrlObject::setPathname(const QString &pathname)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject11setPathnameERK7QString(
    QV4::UrlObject *self,
    const QString *pathname) {
  return self->setPathname(*pathname);
}

//  QString QV4::UrlObject::port() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject4portEv(const QV4::UrlObject *self) {
  return new QString(self->port());
}

//  bool QV4::UrlObject::setPort(const QString &port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject7setPortERK7QString(
    QV4::UrlObject *self,
    const QString *port) {
  return self->setPort(*port);
}

//  QString QV4::UrlObject::protocol() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8protocolEv(const QV4::UrlObject *self) {
  return new QString(self->protocol());
}

//  bool QV4::UrlObject::setProtocol(const QString &protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject11setProtocolERK7QString(
    QV4::UrlObject *self,
    const QString *protocol) {
  return self->setProtocol(*protocol);
}

//  QString QV4::UrlObject::search() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject6searchEv(const QV4::UrlObject *self) {
  return new QString(self->search());
}

//  bool QV4::UrlObject::setSearch(const QString &search)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject9setSearchERK7QString(
    QV4::UrlObject *self,
    const QString *search) {
  return self->setSearch(*search);
}

//  QString QV4::UrlObject::username() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV49UrlObject8usernameEv(const QV4::UrlObject *self) {
  return new QString(self->username());
}

//  bool QV4::UrlObject::setUsername(const QString &username)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49UrlObject11setUsernameERK7QString(
    QV4::UrlObject *self,
    const QString *username) {
  return self->setUsername(*username);
}

//  QUrl QV4::UrlObject::toQUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV49UrlObject6toQUrlEv(const QV4::UrlObject *self) {
  return new QUrl(self->toQUrl());
}

//  void QV4::UrlObject::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49UrlObject6setUrlERK4QUrl(
    QV4::UrlObject *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  const Heap::UrlObject *QV4::UrlObject::constD() const
extern "C" Q_DECL_EXPORT
const QV4::Heap::UrlObject *ritual_ZNK3QV49UrlObject6constDEv(
    const QV4::UrlObject *self) {
  return self->constD();
}
