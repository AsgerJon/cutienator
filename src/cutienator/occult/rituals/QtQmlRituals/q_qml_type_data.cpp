//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypedata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlcomponentandaliasresolver_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qqmlirloader_p.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlpropertyvalidator_p.h>
#include <QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmltypecompiler_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmltypeloaderqmldircontent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qcryptographichash.h>
#include <memory>
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlpropertymap.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qloggingcategory.h>
#include <QtQml/private/qqmltypecompiler_p.h>
#include <QtQml/private/qqmlobjectcreator_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/private/qqmlcomponentandaliasresolver_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/qtyperevision.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 15, as local:qv4resolvedtypereference.cpp:qtTypeInherits
namespace QV4 {
inline template <typename T>
bool qtTypeInherits(const QMetaObject *mo) {
    while (mo) {
        if (mo == &T::staticMetaObject)
            return true;
        mo = mo->superClass();
    }
    return false;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 16, as local:qqmlpropertycachecreator.cpp:processUrlForClassName
inline template<typename BaseNameHandler, typename FailHandler>
auto processUrlForClassName(
    const QUrl &url, BaseNameHandler &&baseNameHandler, FailHandler &&failHandler)
{
    const QString path = url.path();

    // Not a reusable type if we don't have an absolute Url
    const qsizetype lastSlash = path.lastIndexOf(QLatin1Char('/'));
    if (lastSlash <= -1)
        return failHandler();

    // ### this might not be correct for .ui.qml files
    const QStringView baseName = QStringView{path}.mid(lastSlash + 1, path.size() - lastSlash - 5);

    // Not a reusable type if it doesn't start with a upper case letter.
    return (!baseName.isEmpty() && baseName.at(0).isUpper())
        ? baseNameHandler(baseName)
        : failHandler();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 407, as local:qqmltypedata.cpp:InlineComponentData
namespace {
using InlineComponentData = QV4::CompiledData::InlineComponentData;
}  // namespace

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 769, as _ZN12QQmlTypeData12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE
inline void QQmlTypeData::dataReceived(const SourceCodeData &data)
{
    assertTypeLoaderThread();

    m_backupSourceCode = data;

    if (tryLoadFromDiskCache())
        return;

    if (isError())
        return;

    if (!m_backupSourceCode.exists()) {
        if (m_cachedUnitStatus == QQmlMetaType::CachedUnitLookupError::VersionMismatch)
            setError(QQmlTypeLoader::tr("File was compiled ahead of time with an incompatible version of Qt and the original file cannot be found. Please recompile"));
        else
            setError(QQmlTypeLoader::tr("No such file or directory"));
        return;
    }

    if (!loadFromSource())
        return;

    continueLoadFromIR();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 1263, as _ZN12QQmlTypeData14scriptImportedERK14QQmlRefPointerI14QQmlScriptBlobERKN3QV412CompiledData8LocationERK7QStringSC_
inline void QQmlTypeData::scriptImported(
        const QQmlRefPointer<QQmlScriptBlob> &blob, const QV4::CompiledData::Location &location,
        const QString &nameSpace, const QString &qualifier)
{
    assertTypeLoaderThread();

    ScriptReference ref;
    ref.script = blob;
    ref.location = location;
    ref.qualifier = qualifier.isEmpty() ? nameSpace : qualifier + QLatin1Char('.') + nameSpace;

    m_scripts << ref;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 917, as _ZN12QQmlTypeData19allDependenciesDoneEv
inline void QQmlTypeData::allDependenciesDone()
{
    assertTypeLoaderThread();

    QQmlTypeLoader::Blob::allDependenciesDone();

    if (!m_typesResolved)
        resolveTypes();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 795, as _ZN12QQmlTypeData24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE
inline void QQmlTypeData::initializeFromCachedUnit(const QQmlPrivate::CachedQmlUnit *unit)
{
    assertTypeLoaderThread();

    if (unit->qmlData->qmlUnit()->nObjects == 0) {
        setError(QQmlTypeLoader::tr("Cached QML Unit has no objects"));
        return;
    }

    m_document.reset(
            new QmlIR::Document(urlString(), finalUrlString(), m_typeLoader->isDebugging()));
    QQmlIRLoader loader(unit->qmlData, m_document.data());
    loader.load();
    m_document->javaScriptCompilationUnit
            = QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
                new QV4::CompiledData::CompilationUnit(unit->qmlData, unit->aotCompiledFunctions, unit->validateLookupSignatures),
                QQmlRefPointer<QV4::CompiledData::CompilationUnit>::Adopt);
    continueLoadFromIR();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 43, as _ZN12QQmlTypeDataD2Ev
inline QQmlTypeData::~QQmlTypeData()
{
    m_scripts.clear();
    m_compositeSingletons.clear();
    m_resolvedTypes.clear();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 927, as _ZNK12QQmlTypeData8stringAtEi
inline QString QQmlTypeData::stringAt(int index) const
{
    if (m_compiledData)
        return m_compiledData->stringAt(index);
    return m_document->jsGenerator.stringTable.stringForIndex(index);
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 25, as _ZN3QV421ResolvedTypeReference18doDynamicTypeCheckEv
namespace QV4 {
inline void ResolvedTypeReference::doDynamicTypeCheck()
{
    const QMetaObject *mo = nullptr;
    if (m_typePropertyCache)
        mo = m_typePropertyCache->firstCppMetaObject();
    else if (m_type.isValid())
        mo = m_type.metaObject();
    m_isFullyDynamicType = qtTypeInherits<QQmlPropertyMap>(mo);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlscriptblob.cpp, line 17, as _Z14DBG_DISK_CACHEv
inline const QLoggingCategory &DBG_DISK_CACHE()
{
    static const QLoggingCategory category("qt.qml.diskcache");
    return category;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 224, as _ZN16QQmlTypeCompiler14propertyCachesEv
inline QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
{
    return &m_propertyCaches;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 42, as _ZN16QQmlTypeCompiler7compileEv
inline QQmlRefPointer<QV4::CompiledData::CompilationUnit> QQmlTypeCompiler::compile()
{
    // Build property caches and VME meta object data

    for (auto it = resolvedTypes->constBegin(), end = resolvedTypes->constEnd();
         it != end; ++it) {
        QQmlCustomParser *customParser = (*it)->type().customParser();
        if (customParser)
            customParsers.insert(it.key(), customParser);
    }

    QQmlPendingGroupPropertyBindings pendingGroupPropertyBindings;


    {
        QQmlPropertyCacheCreator<QQmlTypeCompiler> propertyCacheBuilder(
                &m_propertyCaches, &pendingGroupPropertyBindings,
                loader, this, imports(), typeData->typeClassName());
        QQmlError cycleError = propertyCacheBuilder.verifyNoICCycle();
        if (cycleError.isValid()) {
            recordError(cycleError);
            return nullptr;
        }
        QQmlPropertyCacheCreatorBase::IncrementalResult result;
        do {
            result = propertyCacheBuilder.buildMetaObjectsIncrementally();
            const QQmlError &error = result.error;
            if (error.isValid()) {
                recordError(error);
                return nullptr;
            } else {
                // Resolve component boundaries and aliases

                QQmlComponentAndAliasResolver resolver(this, &m_propertyCaches);
                if (QQmlError error = resolver.resolve(result.processedRoot); error.isValid()) {
                    recordError(error);
                    return nullptr;
                }
                pendingGroupPropertyBindings.resolveMissingPropertyCaches(&m_propertyCaches);
                pendingGroupPropertyBindings.clear(); // anything that can be processed is now processed
            }
        } while (result.canResume);
    }

    {
        SignalHandlerResolver converter(this);
        if (!converter.resolveSignalHandlerExpressions())
            return nullptr;
    }

    {
        QQmlEnumTypeResolver enumResolver(this);
        if (!enumResolver.resolveEnumBindings())
            return nullptr;
    }

    {
        QQmlCustomParserScriptIndexer cpi(this);
        cpi.annotateBindingsWithScriptStrings();
    }

    {
        QQmlAliasAnnotator annotator(this);
        annotator.annotateBindingsToAliases();
    }

    {
        QQmlDeferredAndCustomParserBindingScanner deferredAndCustomParserBindingScanner(this);
        if (!deferredAndCustomParserBindingScanner.scanObject())
            return nullptr;
    }

    if (!document->javaScriptCompilationUnit || !document->javaScriptCompilationUnit->unitData()) {
        // Compile JS binding expressions and signal handlers if necessary
        {
            // We can compile script strings ahead of time, but they must be compiled
            // without type optimizations as their scope is always entirely dynamic.
            QQmlScriptStringScanner sss(this);
            sss.scan();
        }

        Q_ASSERT(document->jsModule.fileName == typeData->urlString());
        Q_ASSERT(document->jsModule.finalUrl == typeData->finalUrlString());
        QmlIR::JSCodeGen v4CodeGenerator(document);
        for (QmlIR::Object *object : std::as_const(document->objects)) {
            if (!v4CodeGenerator.generateRuntimeFunctions(object)) {
                Q_ASSERT(v4CodeGenerator.hasError());
                recordError(v4CodeGenerator.error());
                return nullptr;
            }
        }
        document->javaScriptCompilationUnit = v4CodeGenerator.generateCompilationUnit(/*generated unit data*/false);
    }

    // Generate QML compiled type data structures

    QmlIR::QmlUnitGenerator qmlGenerator;
    qmlGenerator.generate(*document, dependencyHasher);

    if (!errors.isEmpty())
        return nullptr;

    return std::move(document->javaScriptCompilationUnit);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 30, as _ZN16QQmlTypeCompilerC1EP14QQmlTypeLoaderP12QQmlTypeDataPN5QmlIR8DocumentEPN3QV412CompiledData24ResolvedTypeReferenceMapERKSt8functionIF10QByteArrayvEE
inline QQmlTypeCompiler::QQmlTypeCompiler(
        QQmlTypeLoader *typeLoader, QQmlTypeData *typeData, QmlIR::Document *parsedQML,
        QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache,
        const QV4::CompiledData::DependentTypesHasher &dependencyHasher)
    : resolvedTypes(resolvedTypeCache)
    , loader(typeLoader)
    , dependencyHasher(dependencyHasher)
    , document(parsedQML)
    , typeData(typeData)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 36, as _ZN28QQmlPropertyCacheCreatorBase27canCreateClassNameTypeByUrlERK4QUrl
inline bool QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(const QUrl &url)
{
    return processUrlForClassName(url, [](QStringView) {
        return true;
    }, []() {
        return false;
    });
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 994, as _ZN12QQmlTypeData12resolveTypesEv
inline bool QQmlTypeData::resolveTypes()
{
    assertTypeLoaderThread();

    Q_ASSERT(!m_typesResolved);

    // Check that all imports were resolved
    QList<QQmlError> errors;
    auto it = m_unresolvedImports.constBegin(), end = m_unresolvedImports.constEnd();
    for ( ; it != end; ++it) {
        const PendingImportPtr &import = *it;
        if (import->priority != 0)
            continue;

        // If the import was potentially remote and all the network requests have failed,
        // we now know that there is no qmldir. We can register its types.
        if (registerPendingTypes(import))
            continue;

        // This import was not resolved
        QQmlError error;
        error.setDescription(QQmlTypeLoader::tr("module \"%1\" is not installed").arg(import->uri));
        error.setUrl(m_importCache->baseUrl());
        error.setLine(qmlConvertSourceCoordinate<quint32, int>(
                import->location.line()));
        error.setColumn(qmlConvertSourceCoordinate<quint32, int>(
                import->location.column()));
        errors.prepend(error);
    }

    if (errors.size()) {
        setError(errors);
        return false;
    }

    // Load the implicit import since it may have additional scripts.
    if (!m_implicitImportLoaded && !loadImplicitImport())
        return false;

    // Add any imported scripts to our resolved set
    const auto resolvedScripts = m_importCache->resolvedScripts();
    for (const QQmlImports::ScriptReference &script : resolvedScripts) {
        QQmlRefPointer<QQmlScriptBlob> blob
                = typeLoader()->getScript(script.location, script.fileName);
        addDependency(blob.data());

        ScriptReference ref;
        //ref.location = ...
        if (!script.qualifier.isEmpty())
        {
            ref.qualifier = script.qualifier + QLatin1Char('.') + script.nameSpace;
            // Add a reference to the enclosing namespace
            m_namespaces.insert(script.qualifier);
        } else {
            ref.qualifier = script.nameSpace;
        }

        ref.script = blob;
        m_scripts << ref;
    }

    // Lets handle resolved composite singleton types
    const auto resolvedCompositeSingletons = m_importCache->resolvedCompositeSingletons();
    for (const QQmlImports::CompositeSingletonReference &csRef : resolvedCompositeSingletons) {
        TypeReference ref;
        QString typeName;
        if (!csRef.prefix.isEmpty()) {
            typeName = csRef.prefix + QLatin1Char('.') + csRef.typeName;
            // Add a reference to the enclosing namespace
            m_namespaces.insert(csRef.prefix);
        } else {
            typeName = csRef.typeName;
        }

        QTypeRevision version = csRef.version;
        if (!resolveType(typeName, version, ref, -1, -1, true, QQmlType::CompositeSingletonType))
            return false;

        if (ref.type.isCompositeSingleton()) {
            ref.typeData = typeLoader()->getType(ref.type.sourceUrl());
            if (ref.typeData->isWaiting() || m_waitingOnMe.contains(ref.typeData.data())) {
                qCDebug(lcCycle) << "Possible cyclic dependency detected between"
                                 << ref.typeData->urlString() << "and" << urlString();
                continue;
            }
            addDependency(ref.typeData.data());
            ref.prefix = csRef.prefix;

            m_compositeSingletons << ref;
        }
    }

    for (auto unresolvedRef = m_typeReferences.constBegin(), end = m_typeReferences.constEnd();
         unresolvedRef != end; ++unresolvedRef) {

        TypeReference ref; // resolved reference

        const bool reportErrors = unresolvedRef->errorWhenNotFound;

        QTypeRevision version;

        const QString name = stringAt(unresolvedRef.key());

        bool *selfReferenceDetection = unresolvedRef->needsCreation ? nullptr : &ref.selfReference;

        if (!resolveType(name, version, ref, unresolvedRef->location.line(),
                         unresolvedRef->location.column(), reportErrors,
                         QQmlType::AnyRegistrationType, selfReferenceDetection) && reportErrors)
            return false;

        if (ref.selfReference) {
            // nothing to do
        } else if (ref.type.isComposite()) {
            ref.typeData = typeLoader()->getType(ref.type.sourceUrl());
            addDependency(ref.typeData.data());
        } else if (ref.type.isInlineComponentType()) {
            QUrl containingTypeUrl = ref.type.sourceUrl();
            Q_ASSERT(!containingTypeUrl.isEmpty());
            if (QQmlMetaType::equalBaseUrls(finalUrl(), containingTypeUrl)) {
                ref.selfReference = true;
            } else {
                containingTypeUrl.setFragment(QString());
                auto typeData = typeLoader()->getType(containingTypeUrl);
                Q_ASSERT(typeData.data() != this);
                ref.typeData = typeData;
                addDependency(typeData.data());
            }
        }

        ref.version = version;
        ref.location = unresolvedRef->location;
        ref.needsCreation = unresolvedRef->needsCreation;
        m_resolvedTypes.insert(unresolvedRef.key(), ref);
    }

    m_typesResolved = true;
    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 815, as _ZN12QQmlTypeData14loadFromSourceEv
inline bool QQmlTypeData::loadFromSource()
{
    assertTypeLoaderThread();

    m_document.reset(
            new QmlIR::Document(urlString(), finalUrlString(), m_typeLoader->isDebugging()));
    m_document->jsModule.sourceTimeStamp = m_backupSourceCode.sourceTimeStamp();
    QmlIR::IRBuilder compiler;

    QString sourceError;
    const QString source = m_backupSourceCode.readAll(&sourceError);
    if (!sourceError.isEmpty()) {
        setError(sourceError);
        return false;
    }

    if (!compiler.generateFromQml(source, finalUrlString(), m_document.data())) {
        QList<QQmlError> errors;
        errors.reserve(compiler.errors.size());
        for (const QQmlJS::DiagnosticMessage &msg : std::as_const(compiler.errors)) {
            QQmlError e;
            e.setUrl(url());
            e.setLine(qmlConvertSourceCoordinate<quint32, int>(msg.loc.startLine));
            e.setColumn(qmlConvertSourceCoordinate<quint32, int>(msg.loc.startColumn));
            e.setDescription(msg.message);
            errors << e;
        }
        setError(errors);
        return false;
    }
    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 860, as _ZN12QQmlTypeData18continueLoadFromIREv
inline void QQmlTypeData::continueLoadFromIR()
{
    assertTypeLoaderThread();

    for (auto const& object: std::as_const(m_document->objects)) {
        for (auto it = object->inlineComponentsBegin(); it != object->inlineComponentsEnd(); ++it) {
            QString const nameString = m_document->stringAt(it->nameIndex);
            auto importUrl = finalUrl();
            importUrl.setFragment(nameString);
            auto import = new QQmlImportInstance(); // Note: The cache takes ownership of the QQmlImportInstance
            m_importCache->addInlineComponentImport(import, nameString, importUrl);
        }
    }

    m_typeReferences.collectFromObjects(m_document->objects.constBegin(), m_document->objects.constEnd());
    m_importCache->setBaseUrl(finalUrl(), finalUrlString());

    // For remote URLs, we don't delay the loading of the implicit import
    // because the loading probably requires an asynchronous fetch of the
    // qmldir (so we can't load it just in time).
    if (!finalUrl().scheme().isEmpty()) {
        QUrl qmldirUrl = finalUrl().resolved(QUrl(QLatin1String("qmldir")));
        if (!QQmlImports::isLocal(qmldirUrl)) {
            if (!loadImplicitImport())
                return;
            // This qmldir is for the implicit import
            auto implicitImport = std::make_shared<PendingImport>();
            implicitImport->uri = QLatin1String(".");
            implicitImport->version = QTypeRevision();
            QList<QQmlError> errors;

            if (!fetchQmldir(qmldirUrl, implicitImport, 1, &errors)) {
                setError(errors);
                return;
            }
        }
    }

    QList<QQmlError> errors;

    for (const QV4::CompiledData::Import *import : std::as_const(m_document->imports)) {
        if (!addImport(import, {}, &errors)) {
            Q_ASSERT(errors.size());

            // We're only interested in the chronoligically last error. The previous
            // errors might be from unsuccessfully trying to load a module from the
            // resource file system.
            QQmlError error = errors.first();
            error.setUrl(m_importCache->baseUrl());
            error.setLine(qmlConvertSourceCoordinate<quint32, int>(import->location.line()));
            error.setColumn(qmlConvertSourceCoordinate<quint32, int>(import->location.column()));
            setError(error);
            return;
        }
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 62, as _ZN12QQmlTypeData20tryLoadFromDiskCacheEv
inline bool QQmlTypeData::tryLoadFromDiskCache()
{
    assertTypeLoaderThread();

    if (!m_backupSourceCode.isCacheable())
        return false;

    if (!m_typeLoader->readCacheFile())
        return false;

    auto unit = QQml::makeRefPointer<QV4::CompiledData::CompilationUnit>();
    {
        QString error;
        const auto sourceChecksum = [this]() { return m_backupSourceCode.checksum(); };
        if (!unit->loadFromDisk(url(), m_backupSourceCode.sourceTimeStamp(), sourceChecksum,
                                &error)) {
            qCDebug(DBG_DISK_CACHE) << "Error loading" << urlString() << "from disk cache:" << error;
            return false;
        }
    }

    if (unit->unitData()->flags & QV4::CompiledData::Unit::PendingTypeCompilation) {
        restoreIR(unit);
        return true;
    }

    return loadFromDiskCache(unit);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 50, as _ZNK12QQmlTypeData15compilationUnitEv
inline QV4::CompiledData::CompilationUnit *QQmlTypeData::compilationUnit() const
{
    return m_compiledData.data();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 55, as _ZNK12QQmlTypeData7qmlTypeERK7QString
inline QQmlType QQmlTypeData::qmlType(const QString &inlineComponentName) const
{
    if (inlineComponentName.isEmpty())
        return m_qmlType;
    return m_inlineComponentData[inlineComponentName].qmlType;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 431, as _ZN12QQmlTypeData12checkScriptsEv
inline bool QQmlTypeData::checkScripts()
{
    // Check all script dependencies for errors
    for (int ii = 0; ii < m_scripts.size(); ++ii) {
        const ScriptReference &script = m_scripts.at(ii);
        Q_ASSERT(script.script->isCompleteOrError());
        if (script.script->isError()) {
            createError(
                    script,
                    QQmlTypeLoader::tr("Script %1 unavailable").arg(script.script->urlString()));
            return false;
        }
    }
    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 457, as _ZN12QQmlTypeData17checkDependenciesEv
inline bool QQmlTypeData::checkDependencies()
{
    // Check all type dependencies for errors
    for (auto it = std::as_const(m_resolvedTypes).begin(), end = std::as_const(m_resolvedTypes).end();
         it != end; ++it) {
        const TypeReference &type = *it;
        Q_ASSERT(!type.typeData
                 || type.typeData->isCompleteOrError()
                 || type.type.isInlineComponentType());

        if (type.typeData && type.typeData->isError()) {
            const QString &typeName = stringAt(it.key());
            createError(type, QQmlTypeLoader::tr("Type %1 unavailable").arg(typeName));
            return false;
        }

        if (!type.selfReference && type.type.isInlineComponentType()) {
            const QString icName = type.type.elementName();
            Q_ASSERT(!icName.isEmpty());

            // We have a CU here. Check if the inline component exists.
            if (type.typeData && type.typeData->compilationUnit()->inlineComponentId(icName) >= 0)
                return true;

            const QString typeName = stringAt(it.key());
            const qsizetype lastDot = typeName.lastIndexOf(u'.');
            createError(
                    type,
                    QQmlTypeLoader::tr("Type %1 has no inline component type called %2")
                            .arg(QStringView{typeName}.left(lastDot), icName));
            return false;
        }
    }

    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 447, as _ZN12QQmlTypeData11createErrorERKNS_13TypeReferenceERK7QString
inline void QQmlTypeData::createError(const TypeReference &type, const QString &message)
{
    createError(type, message, type.typeData ? type.typeData->errors() : QList<QQmlError>());
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 452, as _ZN12QQmlTypeData11createErrorERKNS_15ScriptReferenceERK7QString
inline void QQmlTypeData::createError(const ScriptReference &script, const QString &message)
{
    createError(script, message, script.script ? script.script->errors() : QList<QQmlError>());
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 494, as _ZN12QQmlTypeData24checkCompositeSingletonsEv
inline bool QQmlTypeData::checkCompositeSingletons()
{
    // Check all composite singleton type dependencies for errors
    for (int ii = 0; ii < m_compositeSingletons.size(); ++ii) {
        const TypeReference &type = m_compositeSingletons.at(ii);
        Q_ASSERT(!type.typeData || type.typeData->isCompleteOrError());
        if (type.typeData && type.typeData->isError()) {
            QString typeName = type.type.qmlTypeName();
            createError(type, QQmlTypeLoader::tr("Type %1 unavailable").arg(typeName));
            return false;
        }
    }

    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 510, as _ZN12QQmlTypeData14createQQmlTypeEv
inline void QQmlTypeData::createQQmlType()
{
    if (QQmlPropertyCacheCreatorBase::canCreateClassNameTypeByUrl(finalUrl())) {
        const bool isSingleton = m_document
            ? m_document.data()->isSingleton()
            : (m_compiledData->unitData()->flags & QV4::CompiledData::Unit::IsSingleton);
        m_qmlType = QQmlMetaType::findCompositeType(
                url(), m_compiledData, isSingleton
                        ? QQmlMetaType::Singleton
                        : QQmlMetaType::NonSingleton);
        m_typeClassName = QByteArray(m_qmlType.typeId().name()).chopped(1);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQmlTypeData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlTypeData : QQmlTypeData {
  using QQmlTypeData::stringAt;
};

//  A QQmlTypeData that Python can take functions over in. Every QQmlTypeData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlTypeDataCall0)(const void *, int *);
typedef void (*CuteQQmlTypeDataCall1)(const void *, const QQmlDataBlob::SourceCodeData *, int *);
typedef void (*CuteQQmlTypeDataCall2)(const void *, const QQmlPrivate::CachedQmlUnit *, int *);
typedef void (*CuteQQmlTypeDataCall3)(const void *, int *);
typedef QString * (*CuteQQmlTypeDataCall4)(const void *, int, int *);
typedef void (*CuteQQmlTypeDataCall5)(const void *, int *);
typedef void (*CuteQQmlTypeDataCall6)(const void *, qreal, int *);
#if QT_CONFIG(qml_network)
typedef void (*CuteQQmlTypeDataCall7)(const void *, int, int *);
#endif  // QT_CONFIG(qml_network)
class CuteQQmlTypeData : public QQmlTypeData {
public:
  using QQmlTypeData::QQmlTypeData;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QQmlDataBlob4doneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12dataReceivedERKNS_14SourceCodeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob19allDependenciesDoneEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QQmlTypeLoader4Blob8stringAtEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob9completedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QQmlDataBlob23downloadProgressChangedEd")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(qml_network)
    if (!std::strcmp(key, "_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_network)
    return false;
  }

  //  void QQmlTypeData::done()
  void done() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTypeDataCall0 call = reinterpret_cast<CuteQQmlTypeDataCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlTypeData::done();
  }

  //  void QQmlTypeData::dataReceived(const SourceCodeData &a0)
  void dataReceived(const QQmlDataBlob::SourceCodeData &a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTypeDataCall1 call = reinterpret_cast<CuteQQmlTypeDataCall1>(taken[1]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlTypeData::dataReceived(a0);
  }

  //  void QQmlTypeData::initializeFromCachedUnit(const
  //      QQmlPrivate::CachedQmlUnit *unit)
  void initializeFromCachedUnit(
      const QQmlPrivate::CachedQmlUnit *unit) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTypeDataCall2 call = reinterpret_cast<CuteQQmlTypeDataCall2>(taken[2]);
      call(this, unit, &handled);
      if (handled) return;
    }
    QQmlTypeData::initializeFromCachedUnit(unit);
  }

  //  void QQmlTypeData::allDependenciesDone()
  void allDependenciesDone() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTypeDataCall3 call = reinterpret_cast<CuteQQmlTypeDataCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlTypeData::allDependenciesDone();
  }

  //  QString QQmlTypeData::stringAt(int index) const
  QString stringAt(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTypeDataCall4 call = reinterpret_cast<CuteQQmlTypeDataCall4>(taken[4]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlTypeData::stringAt(index);
  }

  //  void QQmlNotifyingBlob::completed()
  void completed() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTypeDataCall5 call = reinterpret_cast<CuteQQmlTypeDataCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::completed();
  }

  //  void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)
  void downloadProgressChanged(qreal a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTypeDataCall6 call = reinterpret_cast<CuteQQmlTypeDataCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlNotifyingBlob::downloadProgressChanged(a0);
  }

#if QT_CONFIG(qml_network)
  //  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
  void networkError(QNetworkReply::NetworkError a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlTypeDataCall7 call = reinterpret_cast<CuteQQmlTypeDataCall7>(taken[7]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDataBlob::networkError(a0);
  }
#endif  // QT_CONFIG(qml_network)
};

//  QString QQmlTypeData::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQmlTypeData2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQmlTypeData::tr(sourceText, disambiguation, n));
}

//  QQmlTypeData::~QQmlTypeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeDataD1Ev(QQmlTypeData *self) {
  delete self;
}

//  QV4::CompiledData::CompilationUnit *QQmlTypeData::compilationUnit() const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit *ritual_ZNK12QQmlTypeData15compilationUnitEv(
    const QQmlTypeData *self) {
  return self->compilationUnit();
}

//  QQmlType QQmlTypeData::qmlType(const QString &inlineComponentName) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK12QQmlTypeData7qmlTypeERK7QString(
    const QQmlTypeData *self,
    const QString *inlineComponentName) {
  return new QQmlType(self->qmlType(*inlineComponentName));
}

//  QByteArray QQmlTypeData::typeClassName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QQmlTypeData13typeClassNameEv(
    const QQmlTypeData *self) {
  return new QByteArray(self->typeClassName());
}

//  SourceCodeData QQmlTypeData::backupSourceCode() const
extern "C" Q_DECL_EXPORT
QQmlDataBlob::SourceCodeData *ritual_ZNK12QQmlTypeData16backupSourceCodeEv(
    const QQmlTypeData *self) {
  return new QQmlDataBlob::SourceCodeData(self->backupSourceCode());
}

//  void QQmlTypeData::done()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData4doneEv(QQmlTypeData *self) {
  self->done();
}

//  void QQmlTypeData::dataReceived(const SourceCodeData &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE(
    QQmlTypeData *self,
    const QQmlDataBlob::SourceCodeData *a0) {
  self->dataReceived(*a0);
}

//  void QQmlTypeData::initializeFromCachedUnit(const
//      QQmlPrivate::CachedQmlUnit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlTypeData *self,
    const QQmlPrivate::CachedQmlUnit *unit) {
  self->initializeFromCachedUnit(unit);
}

//  void QQmlTypeData::allDependenciesDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData19allDependenciesDoneEv(QQmlTypeData *self) {
  self->allDependenciesDone();
}

//  QString QQmlTypeData::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlTypeData8stringAtEi(
    const QQmlTypeData *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  void QQmlTypeData::scriptImported(const QQmlRefPointer<QQmlScriptBlob>
//      &blob, const QV4::CompiledData::Location &location, const QString
//      &nameSpace, const QString &qualifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData14scriptImportedERK14QQmlRefPointerI14QQmlScriptBlobERKN3QV412CompiledData8LocationERK7QStringSC_(
    QQmlTypeData *self,
    const QQmlRefPointer<QQmlScriptBlob> *blob,
    const QV4::CompiledData::Location *location,
    const QString *nameSpace,
    const QString *qualifier) {
  self->scriptImported(*blob, *location, *nameSpace, *qualifier);
}

//  bool QQmlTypeData::checkScripts()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlTypeData12checkScriptsEv(QQmlTypeData *self) {
  return self->checkScripts();
}

//  bool QQmlTypeData::checkDependencies()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlTypeData17checkDependenciesEv(QQmlTypeData *self) {
  return self->checkDependencies();
}

//  void QQmlTypeData::createError(const TypeReference &type, const QString
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData11createErrorERKNS_13TypeReferenceERK7QString(
    QQmlTypeData *self,
    const QQmlTypeData::TypeReference *type,
    const QString *message) {
  self->createError(*type, *message);
}

//  void QQmlTypeData::createError(const ScriptReference &script, const
//      QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData11createErrorERKNS_15ScriptReferenceERK7QString(
    QQmlTypeData *self,
    const QQmlTypeData::ScriptReference *script,
    const QString *message) {
  self->createError(*script, *message);
}

//  bool QQmlTypeData::checkCompositeSingletons()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlTypeData24checkCompositeSingletonsEv(
    QQmlTypeData *self) {
  return self->checkCompositeSingletons();
}

//  void QQmlTypeData::createQQmlType()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData14createQQmlTypeEv(QQmlTypeData *self) {
  self->createQQmlType();
}

//  a Python function taken by a CuteQQmlTypeData, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTypeData(
    QQmlTypeData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTypeData *>(self)->take(key, call);
}

//  QString QQmlTypeData::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK12QQmlTypeData8stringAtEi(
    const QQmlTypeData *self,
    int index) {
  return new QString(
      static_cast<const OwnQQmlTypeData *>(self)->OwnQQmlTypeData::stringAt(
          index));
}
