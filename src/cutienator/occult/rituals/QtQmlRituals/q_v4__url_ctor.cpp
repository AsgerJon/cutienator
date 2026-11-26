//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4urlobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtCore/QUrl>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/qml/jsruntime/qv4urlobject.cpp, line 560, as _ZN3QV47UrlCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue UrlCtor::virtualCallAsConstructor(const FunctionObject *that, const Value *argv,
                                                int argc, const Value *newTarget)
{
    ExecutionEngine *v4 = that->engine();

    if (argc < 1 || argc > 2)
        return v4->throwError(QLatin1String("Invalid amount of arguments"));

    Scope scope(v4);

    ScopedValue arg1(scope, argv[0]);

    QString arg1String = arg1->toQString();
    QString urlString;

    if (argc == 2) {
        ScopedValue arg2(scope, argv[1]);
        String *arg2StringValue = arg2->stringValue();

        if (arg2StringValue == nullptr)
            return v4->throwTypeError(QLatin1String("Invalid parameter provided"));

        QUrl url = QUrl(arg2StringValue->toQString());
        QUrl relativeUrl = QUrl(arg1String);

        QString baseUrlPath = url.path();
        QString relativePath = relativeUrl.path();

        // If the base URL contains a path the last section of it is discarded
        int lastSlash = baseUrlPath.lastIndexOf(QLatin1Char('/'));
        if (lastSlash != -1)
            baseUrlPath.truncate(lastSlash);

        if (!relativePath.startsWith(QLatin1Char('/')))
            relativePath = relativePath.prepend(QLatin1Char('/'));

        url.setPath(baseUrlPath + relativePath);
        url.setFragment(relativeUrl.fragment());
        url.setQuery(relativeUrl.query());

        urlString = url.toString();
    } else {
        urlString = arg1String;
    }

    ReturnedValue o = Encode(v4->newUrlObject());

    if (!newTarget)
        return o;

    ScopedObject obj(scope, o);
    obj->setProtoFromNewTarget(newTarget);

    UrlObject *urlObject = obj->as<UrlObject>();

    if (!urlObject->setHref(urlString))
        return v4->throwTypeError(QLatin1String("Invalid URL: %1").arg(urlString));

    return obj->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::UrlCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47UrlCtor10__dataTestEv(QV4::UrlCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::UrlCtor *QV4::UrlCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlCtor *ritual_ZNK3QV47UrlCtor11d_uncheckedEv(
    const QV4::UrlCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::UrlCtor *QV4::UrlCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlCtor *ritual_ZNK3QV47UrlCtor1dEv(const QV4::UrlCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::UrlCtor::virtualCallAsConstructor(const FunctionObject
//      *a0, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47UrlCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *a0,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::UrlCtor::virtualCallAsConstructor(a0, argv, argc, a3);
}
